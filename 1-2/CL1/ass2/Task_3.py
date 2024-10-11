import re

f = open('Task_1.txt')
text = re.split(r'\d+\.\n', f.read())
eng = text[0]


"""
Data in text is in this format:
25.	Run
• run 
<root=“run”,cat=“v”,tense=“present”,gnp=“1,sg”> 
• runs 
<root=“run”,cat=“v”,tense=“present”,gnp=“3,sg”> 
• run 
<root=“run”,cat=“v”,tense=“present”,gnp=“2,sg”> 
• run 
<root=“run”,cat=“v”,tense=“present”,gnp=“pl”> 
• ran 
<root=“run”,cat=“v”,tense=“past”> 
• run 
<root=“run”,cat=“v”,aspect=“participle”> 
• running 
<root=“run”,cat=“v”,aspect=“progress”>

convert it to this format:
<pardef n="r/un__v">
      <e>
        <p>
          <l>un</l>
          <r>un<s n="verb"/><s n="singular"/><s n="future"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>unning</l>
          <r>un<s n="verb"/><s n="singular"/><s n="present"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>an</l>
          <r>un<s n="verb"/><s n="singular"/><s n="past"/></r>
        </p>
      </e>
    </pardef>
    <pardef n="/eat__v">
      <e>
        <p>
          <l>ate</l>
          <r>eat<s n="verb"/><s n="singular"/><s n="future"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>eating</l>
          <r>eat<s n="verb"/><s n="singular"/><s n="present"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>ate</l>
          <r>eat<s n="verb"/><s n="singular"/><s n="past"/></r>
        </p>
      </e>
    </pardef>
    <pardef n="play/__v">
      <e>
        <p>
          <l>play</l>
          <r>play<s n="verb"/><s n="singular"/><s n="future"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>ing</l>
          <r><s n="verb"/><s n="singular"/><s n="present"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>ed</l>
          <r><s n="verb"/><s n="singular"/><s n="past"/></r>
        </p>
      </e>
      <e>
        <p>
          <l>s</l>
          <r><s n="verb"/><s n="plural"/></r>
        </p>
      </e>
    </pardef>
"""

def find_max_match(word_forms):
    min_word = min(word_forms, key=len)
    max_match = min_word
    for word in word_forms:
        while max_match and max_match not in word:
            max_match = max_match[:-1]
    return max_match

def convert_format(text):
    word_data = re.findall(r'• (.*?)\n<root=“(.*?)”,cat=“(.*?)”,(.*?)>', text)
    word_forms = [word[0] for word in word_data]
    max_match = find_max_match(word_forms)
    base_word = word_data[0][1][len(max_match):]
    category = word_data[0][2]

    output = f'<pardef n="{max_match}/{base_word}__{category}">\n'
    for word, root, cat, tags in word_data:
        suffix = word[len(max_match):]
        output += f'  <e>\n    <p>\n      <l>{suffix}</l>\n      <r>{base_word}'
        for tag in re.findall(r'(\w+)=“(\w+)', tags):
            output += f'<s n="{tag[1]}"/>'
        output += '</r>\n    </p>\n  </e>\n'
    output += '</pardef>'
    return output

x = """37.	Ox
• ox 
<root="ox",cat="n",gnp="sg">
• oxen 
<root="ox",cat="n",gnp="pl">
• ox’s 
<root="ox",cat="n",gnp="sg",aspect="gen">
• oxen’s 
<root="ox",cat="n",gnp="pl",aspect="gen">"""
print(convert_format(x))