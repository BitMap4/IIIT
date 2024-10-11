from collections import Counter
from itertools   import tee, islice
from math        import log
from typing      import Any, Iterable

class Class:
    def __init__(
        self, 
        name:               str, 
        class_features:     Iterable[tuple[Any]], 
        feature_set:        set[Any]
    ) -> None:
        _SMOOTHING = 0.001
        self.name:          str              = name
        self.feature_count: dict[Any, float] = {k:v+_SMOOTHING for review in class_features for k, v in Counter(review).items()}
        for k in feature_set:
            if k not in self.feature_count:
                self.feature_count[k] = _SMOOTHING
        # print(self.feature_count)

class Classifier:
    def __init__(
        self, 
        train_set:  dict[str, Iterable[tuple[Any]]], 
        class_freq: dict[str, int] = {}
    ) -> None:
        """
        >>> train_set = {
                "class1": (feature1, feature2, ...), 
                "class2": (feature1, feature2, ...), 
                ...
            }
        --------------------------------------------
        >>> class_freq = {
                "class1": freq1, 
                "class2": freq2, 
                ...
            }
        """
        print("\tMaking classifier")
        train_set                                          = {c:tee(fs)[0] for c,fs in train_set.items()}
        _tset_cpy:         dict[str, Iterable[tuple[Any]]] = {c:tee(fs)[1] for c,fs in train_set.items()}
        # train_set                                          = {c:tee(fs)[0] for c,fs in train_set.items()}
        # _tset_cpy:         dict[str, Iterable[tuple[Any]]] = {c:tee(fs)[1] for c,fs in train_set.items()}
        self.feature_set:  set[Any]                        = {f for fs in _tset_cpy.values() for review in fs for f in review}
        self.vocab_size:   int                             = len(self.feature_set)
        print("\tsetting up classes")
        self.classes:      dict[str, Class]                = {c: Class(c, train_set[c], self.feature_set) for c in train_set}
        self.classes_freq: dict[str, float]                = {c: log(class_freq[c]) for c in class_freq} if class_freq else {c: 0 for c in train_set}

    def classify(self, test_set: tuple[Any]) -> str:
        """
        >>> test_set = (feature1, feature2, ...)
        >>> test_set = ("the", "movie", "was", "boring")
        >>> test_set = ("tri", "rig", "igr", "gra", "ram", "am ", "m b", " ba", "bas", "ase", "sed")
        >>> test_set = (text[i:i+3] for i in range(len(text)-2)) # text = "trigram based language identification"
        """
        scores:   list[float] = []
        _classes: list[str]   = []
        for c in self.classes:
            score: float = 0
            D:     float = log(sum(self.classes[c].feature_count.values()))
            _classes.append(c)
            for f in test_set:
                if f not in self.feature_set: continue
                score += log(self.classes[c].feature_count[f]) - D
            scores.append(score + self.classes_freq[c])
        print(scores)
        return _classes[scores.index(max(scores))]
    
    def feature_counts(self) -> None:
        # return list [feature: {class: count}, ...]
        print("Feature\t", '\t'.join(self.classes))
        for f in self.feature_set:
            print(f, '\t', '\t'.join(str(self.classes[c].feature_count[f]) for c in self.classes)) if self.classes["pos"].feature_count[f] > self.classes["neg"].feature_count[f] else None
        # return {f: {c: self.classes[c].feature_count[f] for c in self.classes} for f in self.feature_set}
