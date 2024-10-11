# README

## Tokenizer

The `Token` class contains all the information about each token that we need to write in the spreadsheet.\
The `tokenizer()` function first does some preprocessing on the text:\

- removes `-\n` so that the words are not split into two tokens
- replaces different versions of quotes with standard forms (' and ")
- puts a space after and before punctuations, except for hyphens
- joins apostrophe to the second token if it is a contraction (for eg- man's -> man + 's')
- fixes whitespaces so that multiple spaces or newlines are replaced by a single space

Then it finds tokens using the regex pattern: `/\w+-?\w+|\S+/`

- `\w+` matches any word character (alphanumeric & underscore)
- `-?` matches zero or one hyphen
- `\w+` matches any word character (alphanumeric & underscore)
- `|` is the OR operator
- `\S+` matches any non-whitespace character

So the pattern matches any word with or without a hyphen, or any non-whitespace character.\

If the `sentence` parameter is `True`, then the function returns 3 things: tokens, list of tokenized sentences, list of sentences.\
To tokenize sentences, the function uses the regex pattern: `/(?<=[.?])\s+/`

- `(?<=[.?])` is a positive lookbehind assertion that matches a space (since the following pattern is `\s+`) that is preceded by a period or a question mark
- `\s+` matches one or more whitespace characters

## POS Tagger

I have used the `nltk` library to tag the tokens with the Universal POS tagset.\

## Meaning in Isolation

I have used the wordnet from the `nltk` corpus to find the meanings of each word.\

## Simplified Lesk Algorithm

The `simplified_lesk()` is implemented as shown in fig G.10 in [this text](https://web.stanford.edu/~jurafsky/slp3/G.pdf) (with some changes).\

## Advanced Lesk

The `enhanced_lesk()` function is a modified form of the pseudocode mentioned above. For each sense, it checks the POS tag, and if the sense has a different POS than the POS we tagged earlier, it skips that sense.\
Further, it also checks if the sense is a stop word, and if it is, it skips that sense.\

## Obtaining results

Run the python file in the same directory.\
The program will write data to a tsv file.\
Sanitize the tsv file by replacing `"` with `\"` so that it can be opened in excel without problems.\
Open the tsv file in excel and save it as an xlsx file.\
Replace `\"` with `"` in the xlsx file.\
Now, all the columns except `_GOLD` ones and `Knowledge Sources` will have the data.

<!-- ### POS changes

- 75\. dirty&emsp;VERB -> ADJ
- 76\. frog&emsp;ADJ -> NOUN
- 78\. "&emsp;ADJ -> .
- 107\. to&emsp;PRT -> ADP
- 169\. Poor&emsp;NOUN -> ADJ
- 177\. to&emsp;PRT -> ADP
- 180\. afoot&emsp;NOUN -> ADV
- 201\. crest-fallen&emsp;NOUN -> ADJ
- 207\. *&emsp;VERB -> .
- 214\. because&emsp;ADP -> CONJ
- 238\. clever&emsp;ADV -> ADJ
- 246\. "&emsp;NOUN -> . -->
