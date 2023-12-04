import numpy as np

PERIOD = -1
SYMBOL = -2

file1 = open('test.txt', 'r')
Lines = file1.readlines()

input = [-1] * 12

for line in Lines:
    row = list()
    row.append(-1)
    for l in line:
        if l == '.':
            row.append(PERIOD)
        elif l.isdigit():
            row.append(l)
        elif l == '\n':
            continue
        else:
            row.append(SYMBOL)
    
    row.append(-1)
    input.append(row)



print(input)