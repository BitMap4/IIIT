import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokeniser import *

data = tokeniser('pg98.txt')
with open('Task_2/output.txt', 'w') as f:
    f.write(process2(data))
    print('Task 2 completed')