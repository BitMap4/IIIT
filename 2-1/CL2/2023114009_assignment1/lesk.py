import re
from nltk.tag import pos_tag
from nltk.corpus import wordnet as wn
#* Uncomment the following lines to download the required nltk resources
# import nltk
# nltk.download('averaged_perceptron_tagger')
# nltk.download('universal_tagset')
# nltk.download('wordnet')

class Token:
    def __init__(self, 
                token = '', 
                pos_model = '', 
                pos_gold = '', 
                meaning_in_isolation = '', 
                meaning_in_context = '', 
                meaning_in_context_gold = '', 
                beyond_lesk_algorithm = '', 
                knowledge_source = ''
            ):
        self.token = token
        self.pos_model = pos_model
        self.pos_gold = pos_gold
        self.meaning_in_isolation = meaning_in_isolation
        self.meaning_in_context = meaning_in_context
        self.meaning_in_context_gold = meaning_in_context_gold
        self.beyond_lesk_algorithm = beyond_lesk_algorithm
        self.knowledge_source = knowledge_source
        
    def __str__(self):
        return f"""\
{self.token}\t\
{self.pos_model}\t\
{self.pos_gold or self.pos_model}\t\
{self.meaning_in_isolation}\t\
{self.meaning_in_context}\t\
{self.meaning_in_context_gold or self.beyond_lesk_algorithm}\t\
{self.beyond_lesk_algorithm}\t\
{self.knowledge_source}\n"""

#! 1.1 TOKENIZATION
def regex_replace(text, replacements):
    for replacement in replacements:
        text = re.sub(replacement[0], replacement[1], text)
    return text

def tokenize(text, sentence=False, pattern = r'\w+-?\w+|\S+'):
        text = regex_replace(text, [
            # TODO [x]: when word breaks at the end of sentence into wo- rd
            (r'-\n', r''),
            # TODO [x]: replace different versions of ' and "
            (r'’', r"'"),
            (r'‘', r"'"),
            (r'”', r'"'),
            (r'“', r'"'),
            # TODO [x]: punctuations
            (r'([^\s\w-])', r' \1 '),
            # TODO [x]: dont break hyphenated-words and handle apostrophe for shortening
            # hyphenation fixed in previous TODO
            (r'(\w+) \' (\w+)', r"\1 '\2"),
            # TODO [x]: fix whitespaces
            ('\n+|\s+', ' ')
        ]).strip()

        tokens = re.findall(pattern, text)
        if sentence: 
            sentences_string = re.split(r'(?<=[.?])\s+', text)
            sentences_string = [
                regex_replace(sent, [
                    (r' ([^\s\w-]) ', r'\1 '),
                    (r'(\w+) \'(\w+)', r"\1'\2"),
                    # (r' ([.!?])', r'\1')
                ]) for sent in sentences_string
            ]
            sentences = [re.findall(pattern, sentence) for sentence in sentences_string]
            return tokens, sentences, sentences_string
        return tokens



#! 1.4 SIMPLIFIED LESK ALGORITHM
def simplified_lesk(meanings, sentence):
    if not meanings:
        return "UNK"
    
    best_meaning = meanings[0]
    max_overlap = 0
    context = set(sentence)

    for meaning in meanings:
        signature = set(meaning.split())
        overlap = len(signature.intersection(context))

        if overlap > max_overlap:
            max_overlap = overlap
            best_meaning = meaning

    return best_meaning



#! 1.5 BEYOND SIMPLE LESK
def wordnet_pos(tag):
    if   tag == 'ADJ':
        return (wn.ADJ, wn.ADJ_SAT)
    elif tag == 'VERB':
        return (wn.VERB,)
    elif tag == 'NOUN':
        return (wn.NOUN,)
    elif tag == 'ADV':
        return (wn.ADV,)
    else:
        return (None,)

def enhanced_lesk(word, word_pos, sentence):
    senses = wn.synsets(word)
    best_sense = None
    max_overlap = 0

    for sense in senses:
        if sense.pos() not in wordnet_pos(word_pos):
            continue

        definition = set(tokenize(sense.definition()))
        related_words = set([word for words in sense.lemma_names() for word in words])
        for hypernym in sense.hypernyms():
            hypernym_related_words = set([word for words in hypernym.lemma_names() for word in words])
            related_words.update(hypernym_related_words)

        context = set(sentence)
        overlap = len(definition.intersection(context)) + len(related_words.intersection(context))

        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense

    return best_sense



data_sentences = []

with open('10. Haris luck.txt') as f:
    text = f.read()
    _, sentences, setnences_string = tokenize(text, sentence=True)

for i, sentence in enumerate(sentences):
    tokens = sentence
    data = []
    
    for token in tokens:
        data.append(Token(token=token))
        if sum(len(data) for data in data_sentences) >= 250: break



    #! 1.2 POS TAGGING
    pos_tags = pos_tag(tokens, tagset='universal')

    for i, tag in enumerate(pos_tags):
        data[i].pos_model = tag[1]
        if sum(len(data) for data in data_sentences) >= 250: break



    #! 1.3 MEANING IN ISOLATION
    meanings = [
        (
            token, 
            [synset.definition() for synset in wn.synsets(token)]
        ) 
        for token 
        in tokens
    ]

    for i, meaning in enumerate(meanings):
        data[i].meaning_in_isolation = str(meaning[1]) if meaning[1] else 'UNK'
        if sum(len(data) for data in data_sentences) >= 250: break



    #! 1.4 SIMPLIFIED LESK ALGORITHM
    for i, word in enumerate(sentence):
        if pos_tags[i][1] == '.': data[i].meaning_in_context = 'Punctuation'
        else: data[i].meaning_in_context = simplified_lesk(meanings[i][1], sentence)
        if sum(len(data) for data in data_sentences) >= 250: break



    #! 1.5 BEYOND SIMPLE LESK
    for i, word in enumerate(sentence):
        if pos_tags[i][1] == '.': data[i].beyond_lesk_algorithm = 'Punctuation'
        else: 
            sense = enhanced_lesk(word, pos_tags[i][1], sentence)
            if sense: 
                data[i].beyond_lesk_algorithm = sense.definition()
                data[i].knowledge_source = 'K1: POS, K6a: Paradigmatic relations'
            else: 
                data[i].beyond_lesk_algorithm = 'UNK'
                data[i].knowledge_source = 'UNK'
        if sum(len(data) for data in data_sentences) >= 250: break



    data_sentences.append(data)


#! 1.6 ANALYSIS
with open('output.tsv', 'w') as f:
    f.write(f'Story name:\tHaris luck\n')
    num_tokens = 0
    for i, data in enumerate(data_sentences):
        f.write(f'Sentence id:\t{i+1}\n')
        f.write(f'Text:\t{setnences_string[i]}\n')
        f.write('TKN number\tTKN\tPOS_MODEL\tPOS_GOLD\tMeaning in Isolation\tMeaning in Context\tMeaning in Context_GOLD\tBeyond Lesk Algorithm\tKnowledge Source\n')
        for token in data:
            num_tokens += 1
            f.write(f'{num_tokens}\t{token}')
            if num_tokens >= 250: break
        if num_tokens >= 250: break