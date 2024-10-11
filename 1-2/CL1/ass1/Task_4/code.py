import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokeniser import *

data = tokeniser('pg98.txt')
freq = process3(data)
with open('Task_4/output.txt', 'w') as f:
    f.write(process4(data))
    f.write(f'\n\nTotal Type-Token Ratio = {len(freq) / sum([freq[k] for k in freq])}')
    print('Task 4 completed')