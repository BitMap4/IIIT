# Assignment 3 Report
### Q1. Collect character-based unigram, bigram, trigram, and 4-gram character based ngram counts ngram statistics from the training dataset
Files available in [`output/Q1/`](output/q1/)
### Q2. Using character ngram counts from the training data, predict the language of each sentence in the test set using unigram, bigram, trigram and 4-gram character based ngram counts. Report the precision and recall of the classification of each of the above ngram classes in a tabular format. Write a short note on the ngrams with zero count in your test set.
Precision and recall for polish_czech

| ngrams    | Precision | Recall |
| --- | --- | --- |
| Unigrams  | 0.9954357721590916 | 0.995428476435874 |
| Bigrams   | 0.9980883061493411 | 0.9980882719640928 |
| Trigrams  | 0.9988918539039896 | 0.9988917518632422 |
| Quadgrams | 0.9883530343793918 | 0.9883356883606239 |

Precision and recall for spanish_portugese

| ngrams    | Precision          | Recall             |
| --------- | ------------------ | ------------------ |
| Unigrams  | 0.96665866723783   | 0.9666193828815346 |
| Bigrams   | 0.990241912735074  | 0.9902395856378756 |
| Trigrams  | 0.9952695962016461 | 0.9952694525058237 |
| Quadgrams | 0.8252179436028418 | 0.8222173058653583 |

Since this model uses naive Bayes' to classify sentences into languages, zero count ngrams pose a problem- they would make the product of probabilities 0. To avoid this, we use Laplace smoothing (add 1 smoothing) to smoothen the dataset. We initialize all ngram counts with 1, so any ngram encountered in either language in the training data will have count at least 1.

Further, if the test data has any n-gram that wasn't encountered in the training data, the n-gram is ignored and not used for calculating the probability.
### Q3. Write a short note on the cases where you system misclassified sentences. Please use linguistic examples to illustrate your points.
<!-- %% function words, length of words, same words %% -->
*Polish-Czech*
1. Shared Slavic roots:\
	Polish and Czech are both West Slavic languages, sharing many common linguistic features. This close relationship can lead to similarities in the n-grams that might confuse the classifier.

2. Vocabulary overlap:\
	There are many cognates and loanwords between Polish and Czech due to their shared history and geographic proximity. Some words might be identical or very similar in both languages.

3. Similar grammatical structures:\
	Both languages have complex inflectional systems and similar word order, which could lead to structurally similar sentences. So commonly seen patterns in word groups in a language might also be common in the other

4. Phonetic similarities:\
	While your classifier works with text, the underlying phonetic similarities between Polish and Czech might be reflected in their orthography, potentially causing confusion.

5. Dialect continuum:\
	In border regions, there might be dialects that share features of both languages, making classification more challenging for sentences from these areas.

6. Historical influences:\
	Both languages have been influenced by German and Latin, which might result in similar loanwords or calques that are hard to distinguish.

7. Proper nouns:\
	Names of people, places, or organizations might be similar or identical in both languages, potentially leading to misclassification if they're prominent in a sentence.

8. Specialized terminology:\
    In certain fields (e.g., scientific or technical), the terminology might be very similar between the two languages.

9. Orthographic conventions:\
    While there are differences, some orthographic features (like the use of diacritics) are similar in both languages, which might contribute to confusion in certain cases.

The results show that trigrams perform the best, which suggests that capturing slightly longer sequences of characters helps in differentiating between the languages. The slight drop in performance for quadgrams shows that this length starts to be too specific, thus overfitting to the training data.

*Spanish-Portuguese*
1. Shared Latin roots:\
 	Spanish and Portuguese are both Iberian Romance languages, sharing a significant portion of their vocabulary and grammar due to their common Latin ancestry.

2. Geographic proximity:\
 	The languages have influenced each other throughout history due to the shared border between Spain and Portugal.

3. Similar phonetic systems:\
 	Many sounds are pronounced similarly in both languages, which can be reflected in their orthography.

4. Cognates and false friends:\
 	There are numerous words that are identical or very similar in both languages, some with the same meanings and others with different meanings.

5. Parallel grammatical structures:\
 	Both languages have similar syntax and grammatical features, such as gender agreement and verb conjugations.

6. Shared loanwords:\
 	Both languages have borrowed words from Arabic, indigenous American languages, and more recently, English.

7. Regional varieties:\
 	Some dialects of Spanish (e.g., Galician) are particularly close to Portuguese, which could lead to misclassifications.

8. Code-switching in border regions:\
 	In areas where both languages are spoken, mixing of the two languages is common.

9. Similar orthographic conventions:\
 	While there are differences, many spelling rules are similar.

10. Specialized or technical vocabulary:\
 	In certain fields, terminology might be very similar or identical.

We see a similar drop in quadgram precision and recall for the same reasons.
### Q4. Analyze the cases where the system successfully classified the sentences and illustrate the linguistic phenomenon that are modeled by character ngrams (You may need to additional materials to learn more about the language pairs in question)
# Polish-Czech
## 1. Orthographic Differences
Character n-grams are particularly effective at capturing orthographic differences between Polish and Czech. These differences often reflect distinct phonological features of the languages.
### Successful Classification Examples:
- Czech "ř" (no equivalent in Polish)
  - Czech: "řeka" (river) vs. Polish: "rzeka"
  - N-grams: "řek", "eka" (Czech) vs. "rze", "zek", "eka" (Polish)
  - Sentences correctly classified in test set:\
	  pol: Ta rzeka wpada do Renu.
	  ces: Která řeka je nejdelší na světě?
## 2. Morphological Differences
Character n-grams can capture morphological differences, especially in prefixes and suffixes.
### Successful Classification Examples:
- Verb infinitive endings
  - Polish: "-ć" vs. Czech: "-t"
  - Polish: "robić" (to do) vs. Czech: "dělat"
  - N-grams: "bić", "ić" (Polish) vs. "lat", "at" (Czech)
  - Sentences correctly classified:\
	  pol: Nie możemy tego zrobić ponownie.
	  ces: Může to Tom udělat dnes?
## 3. Phonological Representations
N-grams model how phonological differences are represented in writing.
### Successful Classification Examples:
- Polish "h" often corresponds to Czech "ch" in cognates
  - Polish: "historia" vs. Czech: "historie" (history)
  - N-grams: "his", "ist" (Polish) vs. "chi", "ist" (Czech)
  - Sentences:\
	  pol: Jego historia nie może być prawdziwa.
	  ces: Starsi ludzie chętnie opowiadali historie o odwadze.
## 4. Consonant Clusters
Both languages have complex consonant clusters, but their patterns differ.
### Successful Classification Examples:
- Polish tends to have more complex clusters
  - Polish: "mgła" (fog) vs. Czech: "mlha"
  - N-grams: "mgł" (Polish) vs. "mlh" (Czech)
  - Sentences:\
	  pol: "Panie dyrektorze, wyszła mgła."
	  ces: Loď pohltila mlha.
## 5. Diacritical Marks
The distribution and frequency of diacritical marks differ between the languages.
### Successful Classification Examples:
- Czech uses the háček (ˇ) more frequently
  - Czech: "čas" vs. Polish: "czas" (time)
  - N-grams: "ča", "as" (Czech) vs. "cza", "zas" (Polish)
  - Sentences:\
	  pol: Dále čekat se zdá být ztrátou času.
	  ces: Czy będziesz miał pojutrze czas?

# Spanish-Portuguese

## 1. Orthographic Differences
Character n-grams effectively capture subtle orthographic differences between Spanish and Portuguese, which often reflect distinct phonological features.
### Successful Classification Examples:
- Spanish "ñ" vs. Portuguese "nh"
  - Spanish: "año" vs. Portuguese: "ano" (year)
  - N-grams: "año" (Spanish) vs. "ano" (Portuguese)
  - Sentences:\
	  spa: Aquel año la Navidad cayó en sábado.
	  por: "Em geral, neste ano, os pomatos estão crescendo bem."
## 2. Vowel Differences
Portuguese has a more complex vowel system, including nasal vowels, which is reflected in the orthography.
### Successful Classification Examples:
- Portuguese nasal vowels (ã, õ) vs. Spanish vowel + n
  - Portuguese: "mão" vs. Spanish: "mano" (hand)
  - N-grams: "mão" (Portuguese) vs. "man" (Spanish)
  - Sentences:\
	  por: Tom vai pedir a mão de Mary.
	  spa: Se votará a mano alzada.
- Portuguese "ou" vs. Spanish "o"
  - Portuguese: "ouro" vs. Spanish: "oro" (gold)
  - N-grams: "our" (Portuguese) vs. "oro" (Spanish)
  - sentences:\
	  por: Este ouro é meu.
	  spa: Le puso una cadena de oro al cuello.
## 4. Diacritical Marks
The distribution and frequency of diacritical marks differ between the languages.
### Successful Classification Examples:
- Portuguese uses more varied diacritics (á, à, â, ã, ç, é, ê, í, ó, ô, õ, ú)
  - Portuguese: "não" vs. Spanish: "no" (no)
  - N-grams: "não" (Portuguese) vs. "no" (Spanish)
  - Sentences:\
	  por: Eu não estou brigando com você.
	  spa: No puedo terminar esta parte del rompecabezas.
## 5. Phonetic Representations
N-grams model how phonological differences are represented in writing.
### Successful Classification Examples:
- Portuguese maintains some initial consonant clusters that Spanish has modified
  - Portuguese: "plano" vs. Spanish: "llano" (flat)
  - N-grams: "pla" (Portuguese) vs. "lla" (Spanish)
  - Sentences:\
	  por: Qual é o seu plano agora?
	  spa: Dígalo en lenguaje llano.
