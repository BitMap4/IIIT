from collections import Counter
from math        import log

def ngrams(text: str, n: int) -> list[str]:
    return [text[i:i+n] for i in range(len(text) - n + 1) if not any (c in text[i:i+n] for c in ".,!?")]

class Language:
    def __init__(self, text: str, p: 'LanguageClassifier') -> None:
        self.unigrams : dict[str, int] = {k:v+1 for k, v in Counter(ngrams(text, 1)).items()}
        self.bigrams  : dict[str, int] = {k:v+1 for k, v in Counter(ngrams(text, 2)).items()}
        self.trigrams : dict[str, int] = {k:v+1 for k, v in Counter(ngrams(text, 3)).items()}
        self.quadgrams: dict[str, int] = {k:v+1 for k, v in Counter(ngrams(text, 4)).items()}
        # self.sizes    : list[int]      = [len(_ngrams) for _ngrams in [self.unigrams, self.bigrams, self.trigrams, self.quadgrams]]
        _ngrams_list = [self.unigrams, self.bigrams, self.trigrams, self.quadgrams]
        for i, pred_ngrams in enumerate([p.unigrams, p.bigrams, p.trigrams, p.quadgrams]):
            for key in pred_ngrams:
                if key not in _ngrams_list[i]:
                    _ngrams_list[i][key] = 1

class LanguageClassifier:
    def __init__(self, texts: list[str]) -> None:
        print("\tMaking classifier")
        self.languages: list[Language] = []
        self.unigrams : set[str]       = set()
        self.bigrams  : set[str]       = set()
        self.trigrams : set[str]       = set()
        self.quadgrams: set[str]       = set()
        for text in texts:
            self.unigrams  = self.unigrams .union(ngrams(text, 1))
            self.bigrams   = self.bigrams  .union(ngrams(text, 2))
            self.trigrams  = self.trigrams .union(ngrams(text, 3))
            self.quadgrams = self.quadgrams.union(ngrams(text, 4))
        print("\tSetting up languages")
        for text in texts:
            self.languages.append(Language(text, self))

    def vocab_size(self, i: int) -> int:
        return len(self.unigrams) - i + 1

    def classify(self, text: str, ignore: list[int] = []) -> int:
        _ngrams_list: list[dict[str, int]] = [Counter(ngrams(text, 1)), Counter(ngrams(text, 2)), Counter(ngrams(text, 3)), Counter(ngrams(text, 4))]
        _scores     : list[float]          = []

        for language in self.languages:
            score: float = 0
            for i, _lang_ngrams in enumerate([language.unigrams, language.bigrams, language.trigrams, language.quadgrams]):
                if i in ignore: continue
                D: float = log(sum(_lang_ngrams.values()))
                for n in _ngrams_list[i]:
                    # count_n: int = (_lang_ngrams[n] if n in _lang_ngrams else 1)
                    if n not in _lang_ngrams: continue
                    score += log(_lang_ngrams[n]) - D
                    # score += count_n / D
            _scores.append(score)

        return _scores.index(max(_scores))