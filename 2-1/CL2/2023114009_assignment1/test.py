import nltk
nltk.download('punkt')

#! 1.1 TOKENIZATION
with open('10. Haris luck.txt') as f:
    text = f.read()
    tokens = nltk.word_tokenize(text)
    
    
with open('output2.txt', 'w') as f:
    i=0
    for token in tokens:
        i += 1
        f.write(token + ' ')
        if i==250: break










