import numpy as np
import pandas as pd
import time
from re import sub
from sklearn.metrics import precision_score, recall_score, f1_score


def mapping(training_data):
    mapping = {
        '_': 'UNK',
        'ADP': 'PSP',
        'SYM': 'SYM',
        'CCONJ': 'CC',
        'ADJ': 'JJ',
        'INTJ': 'INJ',
        'DET': 'DT',
        'NOUN': 'NN',
        'NUM': 'QT',
        'AUX': 'VAU*',
        'PRON': 'PR',
        'SCONJ': 'CCS',
        'X': 'UNK',
        'PUNC': 'PUNC',
        'ADV': 'RB',
        'PUNCT': 'PUNC',
        'PART': 'RP',
        'PROPN': 'NNP',
        'VERB': 'VM'
    }
    for key in mapping:
        training_data = training_data.replace(key, mapping[key])
    training_data = training_data.replace('VAU*', 'VAUX')
    return training_data

with open("english_data.txt") as f:
    training_data = sub('\t\n', '', f.read())
    training_data = mapping(training_data).split('\n\n')
    training_data = [[x.split('\t')
                        for x in sentence.split('\n') if x] 
                    for sentence in training_data]

training_pairs = [x for sentence in training_data for x in sentence]

for i in range(len(training_pairs)):
    if len(training_pairs[i]) != 2:
        print(i)

tags = [t for _, t in training_pairs]
tagset = set(tags)

def emission_p(tag, word, training_data = training_pairs):
    words_with_tag = [w for w, t in training_data if t == tag]
    word_count = len([1 for w in words_with_tag if w == word])
    tag_count = len(words_with_tag)
    return word_count/tag_count

def transition_p(tag1, tag2, tags = list(tags)):
    t2_occured, t1_after_t2 = 0, 0
    for i in range(len(tags) - 1):
        if tags[i] == tag2:
            t2_occured += 1
            if tags[i+1] == tag1:
                t1_after_t2 += 1
    if t2_occured == 0: return 0
    return t1_after_t2/t2_occured

def initial_p_list(training_data = training_data):
    p_tag = {}
    for tag in tagset:
        p_tag[tag] = len([1 for sent in training_data if sent[0][1] == tag])/len(training_data)
    return p_tag

tags_matrix = np.zeros((len(tagset), len(tagset)), dtype = 'float32')
for i, tag1 in enumerate(tagset):
    for j, tag2 in enumerate(tagset):
        tags_matrix[i, j] = transition_p(tag1, tag2)

tags_df = pd.DataFrame(tags_matrix, columns = list(tagset), index = list(tagset))
initial_p = initial_p_list()

def viterbi(sentence, tagset = list(tagset)):
    state = []
    for i, word in enumerate(sentence):
        p = []
        for tag in tagset:
            if i == 0:
                transition_prb = initial_p[tag]
            else:
                transition_prb = tags_df.loc[state[-1], tag]
            emission_prb = emission_p(tag, word)
            p.append(emission_prb * transition_prb)
        p_max = max(p)
        state_max = tagset[p.index(p_max)]
        state.append(state_max)
    return list(zip(sentence, state))

with open('english.txt') as f:
    testing_data = f.read()[:-2].split('\n\n')
    testing_data = [[x.split('\t')
                        for x in sentence.split('\n') if x] 
                    for sentence in testing_data]
    # print(set([t for _,t in [x for sentence in testing_data for x in sentence]]))
    # print(tagset)

start = time.time()
correct, total = 0, 0
x = 0
predicted_tags = []
actual_tags = []
for sentence in testing_data:
    x+=1
    predicted = viterbi([x[0] for x in sentence])
    for i in range(len(sentence)):
        predicted_tags.append(predicted[i][1])
        actual_tags.append(sentence[i][1])
        try: 
            if (sentence[i][1] == predicted[i][1]): pass
        except IndexError: print(sentence[i], predicted[i])
    correct += len([1 for i in range(len(sentence)) if sentence[i][1] == predicted[i][1]])
    total += len(sentence)

precision = precision_score(predicted_tags, actual_tags, average="weighted", zero_division=0)
print("Precision:", precision)
recall = recall_score(predicted_tags, actual_tags, average="weighted", zero_division=0)
print("Recall:", recall)
f1 = f1_score(predicted_tags, actual_tags, average="weighted", zero_division=0)
print("F1 Score:", f1)

tags= list(set(actual_tags))
tags.sort()
c= pd.DataFrame(np.zeros((len(tags), len(tags))), index=tags, columns=tags)
for i in range(len(actual_tags)):
    if actual_tags[i] in c.index and predicted_tags[i] in c.columns:
        c.loc[actual_tags[i], predicted_tags[i]]+= 1
print(c)

end = time.time()

print(f"Time taken in seconds: {end-start}")
