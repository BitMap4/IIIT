import matplotlib.pyplot as plt

with open('english.txt') as f:
    english = {}
    for i in f:
        x = i.strip().split('\t')
        if len(x)==2:
            if x[1] in english: english[x[1]] += 1
            else: english[x[1]] = 1

with open('hindi.txt') as f:
    hindi = {}
    for i in f:
        x = i.strip().split('\t')
        if len(x) == 2:
            if x[1] in hindi: hindi[x[1]] += 1
            else: hindi[x[1]] = 1

plt.bar(english.keys(), english.values())
plt.title('English Word Frequencies')
plt.savefig('plot.png')

plt.bar(hindi.keys(), hindi.values())
plt.title('Hindi Word Frequencies')
plt.show()