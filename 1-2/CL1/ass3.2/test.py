
from sklearn.metrics import precision_score, recall_score, f1_score
import pandas as pd
import numpy as np
import re

first_tags = []
second_tags = []

# with open("hindi_data.txt") as f:
#     training_data = re.sub('[A-Z]+_', '', f.read())
#     f1 = open("test.txt", "w")
#     f1.write(training_data)
#     f1.close()

with open('test.txt', "r") as file:
    text = re.sub(' +', '\t', file.read())

with open("test.txt", "w") as file:
    file.write(text)

with open("test.txt", "r", encoding='utf-8') as file:
    for line in file:
        if not line: 
            continue
        parts = line.split()
        if len(parts) == 3:  
            first_tags.append(parts[1])
            second_tags.append(parts[2])

precision = precision_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Precision:", precision)

recall = recall_score(first_tags, second_tags, average="weighted", zero_division=0)

print("Recall:", recall)

f1 = f1_score(first_tags, second_tags, average="weighted", zero_division=0)

print("F1 Score:", f1)

def confusion_matrix(actual, predicted):
    tags= list(set(actual))
    tags.sort()
    c= pd.DataFrame(np.zeros((len(tags), len(tags))), index=tags, columns=tags)
    for i in range(len(actual)):
        if actual[i] in c.index and predicted[i] in c.columns:
            c.loc[actual[i], predicted[i]]+= 1
    return c

print(confusion_matrix(first_tags, second_tags))