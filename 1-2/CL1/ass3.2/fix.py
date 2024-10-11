
import numpy as np
import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score


training_file = open("english_training.txt", "r")
data = training_file.read()
training_file.close()



sentences = data.strip().split('\n\n')

tagged_sentences = []
for sentence in sentences:
    words = sentence.strip().split('\n')
    tagged_words = [word.split('\t') for word in words]
    tagged_sentences.append(tagged_words)

# print(tagged_sentences)
tagged_words = [x for sentence in tagged_sentences for x in sentence]
tags = set([x[1] for x in tagged_words])

#emission probability:
def word_given_tag(word, tag, train_bag):
    # Initialize variables to count occurrences
    count_tag = 0
    count_w_given_tag = 0
    
    # Iterate through the training tagged words
    for pair in train_bag:
        # Check if the current pair matches the given tag
        if pair[1] == tag:
            count_tag += 1
            # Check if the current word in the pair matches the given word
            if pair[0] == word:
                count_w_given_tag += 1
    
    if count_tag == 0: return 0
    return count_w_given_tag/count_tag


#transition probabilty:
def t2_given_t1(t2, t1, tags):
    tags = list(tags)
    # Count occurrences of t1
    count_t1 = sum([1 for t in tags if t==t1])
            
    # Count occurrences of t2 following t1
    count_t2_t1 = sum([1 for i in range(len(tags)-1) if tags[i]==t1 and tags[i + 1]==t2])
    
    if count_t1 == 0: return 0
    return count_t2_t1/count_t1



def Viterbi(words, tags, train_bag, tags_df):
    tagged_words = []

    for word in words:
        max_prob = 0
        max_tag = None
        
        for tag in tags:
            print(tagged_words)
            # Calculate emission probability
            emission_prob = word_given_tag(word, tag, train_bag)
            
            # Calculate transition probability
            if len(tagged_words) == 0:
                transition_prob = tags_df.loc['PUNCT', tag]
            else:
                prev_tag = tagged_words[-1][1]
                transition_prob = tags_df.loc[prev_tag, tag]

            # Calculate state probability
            state_prob = emission_prob * transition_prob
            
            # Update max probability and tag
            if state_prob > max_prob:
                max_prob = state_prob
                max_tag = tag
        
        tagged_words.append((word, max_tag))

    return tagged_words

def create_tags_matrix(tags):
    num_tags = len(tags)
    tags_matrix = np.zeros((num_tags, num_tags), dtype='float32')

    for i, t1 in enumerate(tags):
        for j, t2 in enumerate(tags):
            tags_matrix[i,j] = t2_given_t1(t2, t1, tags)

    return tags_matrix

tags_matrix=create_tags_matrix(tags)
tags_df = pd.DataFrame(tags_matrix, columns = list(tags), index=list(tags))

print(tags_df)

testing_file = open("english.txt", "r")
test_data = testing_file.read()
testing_file.close()



test_sentences = data.strip().split('\n\n')

test_tagged_sentences = []
for sentence in test_sentences:
    words = sentence.strip().split('\n')
    tagged_words = [word.split('\t') for word in words]
    test_tagged_sentences.append(tagged_words)

# print(tagged_sentences)
testing_pairs = [x for sentence in tagged_sentences for x in sentence]




second_tags = [t for _,t in testing_pairs]
first_tags = Viterbi([w for w,_ in testing_pairs], tags, tagged_words, tags_df)

precision = precision_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Precision:", precision)

recall = recall_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Recall:", recall)

f1 = f1_score(first_tags, second_tags, average="weighted", zero_division=0)

print("F1 Score:", f1)


"""
This is the tags_df matrix that i'm getting

PUNCT  ADV  CCONJ  VERB  PROPN  SCONJ  INTJ  ADP  NUM  SYM  ADJ   ``  PRON  AUX  NOUN  DET    X    '  PART    _
PUNCT    0.0  1.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
ADV      0.0  0.0    1.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
CCONJ    0.0  0.0    0.0   1.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
VERB     0.0  0.0    0.0   0.0    1.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
PROPN    0.0  0.0    0.0   0.0    0.0    1.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
SCONJ    0.0  0.0    0.0   0.0    0.0    0.0   1.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
INTJ     0.0  0.0    0.0   0.0    0.0    0.0   0.0  1.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
ADP      0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  1.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
NUM      0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  1.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
SYM      0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  1.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
ADJ      0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  1.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
``       0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   1.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0
PRON     0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  1.0   0.0  0.0  0.0  0.0   0.0  0.0
AUX      0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   1.0  0.0  0.0  0.0   0.0  0.0
NOUN     0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  1.0  0.0  0.0   0.0  0.0
DET      0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  1.0  0.0   0.0  0.0
X        0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  1.0   0.0  0.0
'        0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   1.0  0.0
PART     0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  1.0
_        0.0  0.0    0.0   0.0    0.0    0.0   0.0  0.0  0.0  0.0  0.0  0.0   0.0  0.0   0.0  0.0  0.0  0.0   0.0  0.0

fix the code to fix the transition probability matrix
"""