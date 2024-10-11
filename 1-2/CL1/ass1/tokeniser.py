import re

def tokeniser(file):
    f = open(file, 'r')
    # pre-processing
    text = f.read()

    text = "\n".join(text.split('\n')[102:])
    text = re.sub(r'CHAPTER.{0,5}\n.*\n', '', text)
    text = re.sub(r'Book the .*--.*\n', '', text)

    # remove . from Mr. Mrs. Dr. etc
    # text = re.sub(r'[A-HJ-Z]([a-z]){0,2}\. ', '', text)
    t = r'(?<=[A-HJ-Z])\. |(?<=[A-HJ-Z][a-z])\. |(?<=[A-HJ-Z]([a-z]){2})\. '
    text = re.sub(t, ' ', text)

    text = text.replace('\n', ' ')
    text = re.sub(r'[^a-zA-Z0-9\s’“”\/\.?!%,-]', '', text)
    text = text.replace('-', ' - ').replace('.', ' . ').replace('!', ' ! ').replace('?', ' ? ').replace('“', ' “ ').replace('”', ' ” ').replace(',', ' , ')
    text = re.sub(r'(?<=[a-zA-Z])’(?=[a-zA-Z])', '=', text)

    text = re.sub(r'http\S+', '<URL>', text)
    text = re.sub(r'www\S+', '<URL>', text)
    text = re.sub(r'\d{1,2}\/\d{1,2}\/\d{2,4}', '<DATE>', text)
    text = re.sub(r'\d{1,2}:\d{2}', '<TIME>', text)
    text = re.sub(r'\d{1,3}\%', '<PERCENT>', text)


    text = text.replace(".", ".*").replace("?", "?*")

    text = re.sub(' +', ' ', text)

    data = [
        {'sentence':i.strip().replace(' - ', '-').replace(' .', '.').replace(' !', '!').replace(' ?', '?').replace('“ ', '“').replace(' ”', '”').replace(' ,', ','), 
         'tokens':i.strip().split(' ')}
        for i in text.split('*') 
        if len(i.strip())>0
        ] # Task 1, 2
    for i in data:
        line = [j.lower() for j in i['tokens']]
        i['ttratio'] = len(set(line)) / len(line) # Task 3

    f.close()

    return data

def frequency(data):
    freq = {}
    for i in data:
        for j in i['tokens']:
            j = j.lower()
            if j in freq:
                freq[j] += 1
            else:
                freq[j] = 1
    return freq # Task 4


def process1(data):
    # only the sentences, not tokens or tt ratio
    sents = '\n'
    for i in range(len(data)):
            sents += f'<Sent id="{i+1}">\n\tText = "{data[i]["sentence"]}"\n</Sent>\n'
    return sents.strip('\n')

def process2(data):
    sents = '\n'
    for i in range(len(data)):
            sents += f'<Sent id="{i+1}">\n\tText = "{data[i]["sentence"]}"\n'
            for j in range(len(data[i]['tokens'])):
                sents += f'\tToken {j+1} = "{data[i]["tokens"][j]}"\n'
    return sents.strip('\n')

def process3(data):
    return frequency(data)

def process4(data):
    sents = '\n'
    for i in range(len(data)):
            sents += f'<Sent id="{i+1}">\n\tText = "{data[i]["sentence"]}"\n'
            for j in range(len(data[i]['tokens'])):
                sents += f'\tToken {j+1} = "{data[i]["tokens"][j]}"\n'
            sents += f'\tType-Token Ratio = {data[i]["ttratio"]}\n</Sent>\n'
    return sents.strip('\n')