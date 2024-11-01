# Analysis of Word Embedding Similarity Scores Across Different Window Sizes

## Methodology
The analysis was conducted using co-occurrence matrices with SVD decomposition, testing three different context window sizes (2, 5, and 8) to examine how window size affects semantic relationships between word pairs.

## Results Summary

| Word Pair           | Window 2 | Window 5 | Window 8 | Trend |
|---------------------|----------|----------|----------|--------|
| market - industry   | 0.5563   | 0.5598   | 0.3930   | ↓ |
| good - bad          | 0.8835   | 0.5010   | 0.4013   | ↓ |
| windows - linux     | 0.7884   | 0.8157   | 0.6333   | ∩ |
| government - policy | 0.2196   | 0.3265   | 0.1805   | ∩ |
| peace - conflict    | -0.0226  | -0.0246  | 0.1378   | ↑ |

## Analysis by Word Pair

### 1. market - industry
- Maintains moderate similarity (~0.56) at smaller windows (2-5)
- Significant drop to 0.3930 at window size 8
- Suggests these terms are more strongly related in immediate contexts rather than broader discourse

### 2. good - bad (Antonyms)
- Strongest correlation (0.8835) at window size 2
- Sharp decrease as window size increases
- Indicates these antonyms frequently appear in close proximity, supporting the distributional hypothesis that opposites often occur in similar contexts

### 3. windows - linux (Technical Terms)
- Strong correlation across all window sizes
- Peak similarity (0.8157) at window size 5
- Demonstrates robust semantic relationship between these operating system terms
- Slight decrease at larger window size suggests optimal capture of technical context at medium ranges

### 4. government - policy
- Generally weak to moderate correlation across all windows
- Peaks at window size 5 (0.3265)
- Lower correlations suggest these terms might appear in more diverse contexts than anticipated

### 5. peace - conflict (Antonyms)
- Interesting progression from slightly negative to positive correlation
- Only pair showing positive trend with increasing window size
- Suggests these concepts are more related in broader discourse than in immediate context

## Key Findings

1. **Window Size Impact**: Most word pairs show strongest correlations at smaller window sizes (2-5), suggesting that immediate context is often more relevant for semantic relationships.

2. **Antonym Behavior**: Antonym pairs (good-bad, peace-conflict) show distinctly different patterns, with good-bad showing strong immediate correlation while peace-conflict shows stronger association in broader contexts.

3. **Domain-Specific Terms**: Technical terms (windows-linux) maintain strong correlation across window sizes, indicating robust semantic relationships regardless of context window.

## Implications
The results demonstrate that optimal window size varies depending on the type of semantic relationship being captured. While technical terms benefit from medium-sized windows, antonyms and business terms show varying patterns that suggest careful window size selection is crucial for specific applications.