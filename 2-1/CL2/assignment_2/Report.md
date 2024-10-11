# English
### A) Token-Type Ratio Calculation

The token-type ratio is a measure of the diversity of vocabulary in a text. It is calculated by dividing the number of words (tokens) by the total number of unique words (types). In the given text, the token-type ratio is:

**Token-Type Ratio:** 8.65

This indicates a low-moderate level of vocabulary diversity. A token-type ratio of 8.65 indicates that, on average, each unique word (type) in the dataset appears 8.65 times.
### B) Frequency Analysis for Words and Letters

After converting the text to lowercase and excluding punctuation marks, the frequencies of both words and letters were calculated.
#### Word Frequency Analysis

The five most frequent words in the text are as follows:
1. **the** - 3986 occurrences
2. **and** - 3191 occurrences
3. **a** - 1936 occurrences
4. **to** - 1809 occurrences
5. **of** - 1589 occurrences

These words are common function words, which contribute to the syntactic structure of sentences but carry less meaning compared to content words. Their high frequency is expected in most English texts, aligning with Zipf's law, where frequently used words are often short and grammatically essential.

#### Letter Frequency Analysis

The five most frequent letters in the text are:
1. **e** - 38,099 occurrences
2. **t** - 30,867 occurrences
3. **o** - 24,964 occurrences
4. **a** - 24,860 occurrences
5. **n** - 21,501 occurrences

The letter frequencies also follow a pattern where vowels and commonly used consonants like 't' and 'n' appear frequently. These results are typical in English texts, where 'e' is consistently the most common letter due to its presence in many grammatical structures.

**Comments on Frequency Patterns**

The high frequency of function words such as "the," "and," and "to" aligns with Zipf's law, which predicts that the most frequent words will account for a significant portion of the text. In contrast, letters are distributed based on their use across all types of words, with vowels and commonly used consonants appearing more frequently. This pattern indicates a structured hierarchy of both word and letter usage that follows a predictable trend across large texts.

#### Plots and Pearson's coefficients of correlation between rank and frequency

![Pasted image 20240906165332.png](images/Pasted_image_20240906165332.png)
![Pasted image 20240906165342.png](images/Pasted_image_20240906165342.png)

![Pasted image 20240906165349.png](images/Pasted_image_20240906165349.png)
![Pasted image 20240906165409.png](images/Pasted_image_20240906165409.png)

### C) Zipf’s Law and Emerging Patterns

Zipf's law is a principle observed in many natural language datasets, where the frequency of a word is inversely proportional to its rank in the frequency table. Basically, the most frequent word occurs twice as often as the second most frequent word, three times as often as the third, and so on. This results in a power-law distribution when plotting word frequency against rank.
#### Observations from Word Data:

In the first pair of plots, we observe Zipf's law in action for words. The untransformed plot shows a steep drop-off in word frequency, which aligns with the general shape expected from Zipf's law. Words with higher ranks occur much less frequently than the most common words. The Pearson correlation coefficient of -0.1708 indicates a weak negative linear relationship between rank and frequency in the non-logarithmic space.

However, the log-log plot provides a much clearer picture of Zipf's law. The almost linear downward slope suggests a strong inverse relationship between the logarithm of the rank and the logarithm of the frequency, as captured by the Pearson correlation coefficient of -0.9886. This is a strong indicator that word frequencies in this dataset closely follow Zipf's law.
#### Observations from Letter Data:

For letters, the frequency distribution also follows a similar downward trend, although the overall pattern differs slightly. The Pearson correlation coefficient of -0.8946 (without log) suggests a stronger negative correlation between rank and frequency compared to words, indicating a closer fit to Zipf's law even in the raw data.

In the log-log plot for letters, the Pearson coefficient is weaker, at -0.7888. This indicates that the frequency of letters is not as tightly bound to Zipf's law as word frequencies.
#### Comparison:

While both words and letters exhibit a power-law distribution, there are noticeable differences:

1. **Strength of Correlation**: The word frequency distribution adheres more strictly to Zipf's law in the log-log space, as evidenced by the stronger correlation (-0.9886) compared to that of letters (-0.7888). This could be due to the fact that words are more context-dependent and appear in a wider variety of frequencies than individual letters, which are more uniform across a given text.
2. **Range of Ranks**: The word rank data spans a much larger range (up to 8000), while the letter rank data is restricted to a much smaller set (around 40 ranks). This difference in scale is expected, as natural language uses a far greater number of distinct words than letters.
#### Conclusion:

Both words and letters follow Zipf's law to a certain degree, with word frequencies displaying a much closer adherence to the law. The deviations in the letter data reflect the more uniform nature of letter usage across the text. These patterns show that words, with their more complex relationships, follow Zipf's law more clearly than letters, which have a simpler and more limited distribution.

### D) Word Frequency vs Word Length

![Pasted image 20240906170458.png](images/Pasted_image_20240906170458.png)

# Hindi
### A) Token-Type Ratio

**Token-Type Ratio:** 4.59
This indicates a moderate level of diversity, almost twice as diverse as the English corpus.

### B) Frequency Analysis for Words and Letters

The 5 most frequent words are:
1. **न**: 464
2. **सब**: 401
3. **दो0**: 295
4. **राम**: 259
5. **सकल**: 218
The 5 most frequent letters are:
1. **र**: 10465
2. **न**: 9785
3. **स**: 8450
4. **ह**: 7633
5. **त**: 5724
#### Plots and Pearson's coefficients
![Pasted image 20240906172234.png](images/Pasted_image_20240906172234.png)
![Pasted image 20240906172239.png](images/Pasted_image_20240906172239.png)

![Pasted image 20240906172256.png](images/Pasted_image_20240906172256.png)
![Pasted image 20240906172259.png](images/Pasted_image_20240906172259.png)
!![[Pasted image 20240906172306.png]]
### C) Patterns

Clearly, the plots are very similar to the ones we saw in English, leading to the same comparisons and conclusion.

### D) Word Frequency vs Word Length

![Pasted image 20240906172725.png](images/Pasted_image_20240906172725.png)