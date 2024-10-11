import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokeniser import *

data = tokeniser('pg98.txt')
with open('Task_1/output.txt', 'w') as f:
    f.write(process1(data))
    print("Task 1 completed")
    # f.write(f'\n\nTotal Type-Token Ratio = {len(freq) / sum([freq[k] for k in freq])}')