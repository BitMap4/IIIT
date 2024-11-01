from typing import List, Dict, Tuple, Optional, Set
from dataclasses import dataclass
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix, lil_matrix
from scipy.sparse.linalg import svds
from scipy.spatial.distance import cosine
from scipy.io import mmwrite
import re
from collections import Counter
from numpy.typing import NDArray
import numpy.typing as npt
from tqdm import tqdm

@dataclass
class AnalysisConfig:
    """Configuration parameters for the analysis."""
    max_lines: Optional[int] = None
    max_vocab_size: int = 50000
    min_word_frequency: int = 2
    window_sizes: List[int] = None
    num_components: int = 50

    def __post_init__(self):
        if self.window_sizes is None:
            self.window_sizes = [2, 4]
        if self.max_lines is not None and self.max_lines <= 0:
            raise ValueError("max_lines must be positive if specified")
        if self.max_vocab_size <= 0:
            raise ValueError("max_vocab_size must be positive")
        if self.min_word_frequency <= 0:
            raise ValueError("min_word_frequency must be positive")
        if not all(w > 0 for w in self.window_sizes):
            raise ValueError("All window sizes must be positive")

@dataclass
class WordPair:
    """Data class for word pairs and their relationship type."""
    word1: str
    word2: str
    relationship: str

class TextPreprocessor:
    def __init__(self, config: AnalysisConfig) -> None:
        self.vocabulary: List[str] = []
        self.word_to_idx: Dict[str, int] = {}
        self.config = config
    
    def _clean_text(self, text: str) -> List[str]:
        """Clean and tokenize text."""
        if not isinstance(text, str):
            raise ValueError("Input text must be a string")
        text = re.sub(r'[^\w\s]', '', text.lower())
        text = re.sub(r'\d+', '', text)
        return [word for word in text.split() if word]
    
    def create_vocabulary(self, sentences: List[str]) -> List[str]:
        """Create vocabulary from sentences."""
        if not sentences:
            raise ValueError("Sentences list cannot be empty")
            
        print("Creating vocabulary...")
        words: List[str] = []
        for sentence in tqdm(sentences, desc="Processing sentences", ncols=100):
            words.extend(self._clean_text(sentence))
        
        word_counts = Counter(words)
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        selected_words = sorted_words[:self.config.max_vocab_size]
        
        self.vocabulary = [word for word, count in selected_words 
                         if count >= self.config.min_word_frequency]
        self.word_to_idx = {word: idx for idx, word in enumerate(self.vocabulary)}
        
        print(f"Vocabulary created with {len(self.vocabulary)} words")
        return self.vocabulary

class CooccurrenceMatrix:
    def __init__(self, preprocessor: TextPreprocessor) -> None:
        self.preprocessor = preprocessor
        self.matrix: Optional[csr_matrix] = None
    
    def create_matrix(self, sentences: List[str], window_size: int) -> csr_matrix:
        """Create co-occurrence matrix using sparse matrix implementation."""
        from collections import defaultdict, Counter

        if not self.preprocessor.vocabulary:
            raise ValueError("Vocabulary not created yet!")

        vocab_size = len(self.preprocessor.vocabulary)
        word_to_idx = self.preprocessor.word_to_idx
        cooccurrences = defaultdict(Counter)

        print("Creating co-occurrence matrix...")
        tokenized_sentences = [
            [word_to_idx[token] for token in self.preprocessor._clean_text(s) if token in word_to_idx]
            for s in sentences
        ]

        for tokens in tqdm(tokenized_sentences, desc="Processing co-occurrences", ncols=100):
            for i, center_idx in enumerate(tokens):
                start = max(0, i - window_size)
                end = min(len(tokens), i + window_size + 1)
                context_indices = tokens[start:i] + tokens[i+1:end]
                for context_idx in context_indices:
                    cooccurrences[center_idx][context_idx] += 1.0

        rows, cols, data = [], [], []
        for center_idx, contexts in cooccurrences.items():
            for context_idx, count in contexts.items():
                rows.append(center_idx)
                cols.append(context_idx)
                data.append(count)

        matrix = csr_matrix((data, (rows, cols)), shape=(vocab_size, vocab_size), dtype=np.float32)
        self.matrix = matrix
        return self.matrix
    
    def print_matrix(self, filename: str) -> None:
        """Print the co-occurrence matrix in a readable format."""
        if self.matrix is None:
            raise ValueError("Co-occurrence matrix not created yet!")
        
        vocabulary = self.preprocessor.vocabulary
        with open(filename, 'w', encoding='utf-8') as f:
            # Write header
            f.write('\t' + '\t'.join(vocabulary) + '\n')
            # Write each row
            for idx, word in enumerate(vocabulary):
                row = self.matrix.getrow(idx).toarray().flatten()
                row_str = '\t'.join(map(str, row))
                f.write(f"{word}\t{row_str}\n")

class WordEmbeddings:
    def __init__(self, config: AnalysisConfig) -> None:
        self.config = config
        self.embeddings: Optional[npt.NDArray[np.float32]] = None
        self.S: Optional[npt.NDArray[np.float32]] = None
    
    def create_embeddings(self, matrix: csr_matrix) -> npt.NDArray[np.float32]:
        """Create word embeddings using truncated SVD."""
        if matrix.shape[0] < self.config.num_components:
            raise ValueError("Matrix dimensions smaller than number of components")
        
        print("Creating word embeddings using SVD...")
        U, self.S, Vt = svds(matrix, k=self.config.num_components)
        
        idx = np.argsort(self.S)[::-1]
        self.embeddings = U[:, idx].astype(np.float32)
        self.S = self.S[idx].astype(np.float32)
        
        return self.embeddings
    
    def get_word_similarity(self, word1: str, word2: str, vocabulary: List[str]) -> Optional[float]:
        """Calculate cosine similarity between two words."""
        if self.embeddings is None:
            raise ValueError("Embeddings not created yet")
            
        if word1 not in vocabulary or word2 not in vocabulary:
            return None
        
        idx1 = vocabulary.index(word1)
        idx2 = vocabulary.index(word2)
        vec1 = self.embeddings[idx1]
        vec2 = self.embeddings[idx2]
        
        return float(1 - cosine(vec1, vec2))

@dataclass
class AnalysisResults:
    """Data class for storing analysis results."""
    vocabulary_size: int
    window_sizes: List[int]
    similarities: Dict[int, Dict[Tuple[str, str], Optional[float]]]
    lines_processed: int

class WordEmbeddingAnalyzer:
    def __init__(self, data_file: str, config: Optional[AnalysisConfig] = None) -> None:
        self.data_file = data_file
        self.config = config or AnalysisConfig()
        
        self.preprocessor = TextPreprocessor(self.config)
        self.cooccurrence = CooccurrenceMatrix(self.preprocessor)
        self.embeddings = WordEmbeddings(self.config)
        self.results: Optional[AnalysisResults] = None
    
    def load_data(self) -> List[str]:
        """Load data with line limit if specified."""
        try:
            print(f"Loading data from {self.data_file}")
            df = pd.read_csv(self.data_file)
            
            if 'Description' not in df.columns:
                raise ValueError("CSV file must contain a 'Description' column")
            
            sentences = df['Description'].tolist()
            
            if self.config.max_lines is not None:
                print(f"Limiting analysis to {self.config.max_lines} lines")
                sentences = sentences[:self.config.max_lines]
            
            print(f"Processing {len(sentences)} lines")
            return sentences
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {self.data_file} not found")
    
    def analyze(self, word_pairs: Optional[List[WordPair]] = None) -> AnalysisResults:
        """Perform complete analysis with different window sizes."""
        sentences = self.load_data()
        vocabulary = self.preprocessor.create_vocabulary(sentences)
        
        if word_pairs is None:
            word_pairs = [
                WordPair("market", "industry", "related"),
                WordPair("good", "bad", "antonym"),
                WordPair("windows", "linux", "related"),
                WordPair("government", "policy", "part-whole"),
                WordPair("peace", "conflict", "antonym")
            ]
        
        similarities: Dict[int, Dict[Tuple[str, str], Optional[float]]] = {}
        
        for window_size in self.config.window_sizes:
            print(f"Processing window size {window_size}")
            matrix = self.cooccurrence.create_matrix(sentences, window_size)
            self.embeddings.create_embeddings(matrix)
            
            window_similarities: Dict[Tuple[str, str], Optional[float]] = {}
            for pair in word_pairs:
                sim = self.embeddings.get_word_similarity(
                    pair.word1, pair.word2, vocabulary
                )
                window_similarities[(pair.word1, pair.word2)] = sim
            
            similarities[window_size] = window_similarities
        
        self.results = AnalysisResults(
            vocabulary_size=len(vocabulary),
            window_sizes=self.config.window_sizes,
            similarities=similarities,
            lines_processed=len(sentences)
        )
        return self.results
    
    def print_results(self) -> None:
        """Print analysis results."""
        if self.results is None:
            raise ValueError("No analysis results available. Run analyze() first.")
            
        print(f"\nLines processed: {self.results.lines_processed}")
        print(f"Vocabulary size: {self.results.vocabulary_size}")
        print("\nSimilarity Scores Analysis:")
        print("-" * 50)
        
        for window_size in self.results.window_sizes:
            print(f"\nWindow Size: {window_size}")
            for (word1, word2), score in self.results.similarities[window_size].items():
                if score is not None:
                    print(f"{word1:10} - {word2:10}: {score:.4f}")
                else:
                    print(f"{word1:10} - {word2:10}: Words not in vocabulary")