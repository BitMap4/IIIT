import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tokeniser import *

data = tokeniser('pg98.txt')
freq = process3(data)

sorted_tokens = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Write the sorted tokens and their frequencies to the output file
with open("Task_3/output.txt", 'w') as f:
    for token, count in sorted_tokens:
        f.write(f'{count} {token}\n')
    print('Task 3 completed')
# with open('Task_3/output.txt', 'w') as f:
#     # write the frequency of each token to the file in descending order

#     print('Task 3 completed')