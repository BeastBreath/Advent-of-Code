from math import lcm
from collections import Counter


CON = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

instructions = list()

def search(n, tree_f, tree_s, letter):
    if letter == "ZZZ":
        return
    print(n)
    print(letter)
    print(instructions[n%len(instructions)])
    print(tree_s[tree_f.index(letter)][instructions[n % len(instructions)]])
    print()
    return search(n + 1, tree_f, tree_s, tree_s[tree_f.index(letter)][instructions[n % len(instructions)]])
    


file1 = open('input.txt', 'r')
Lines = file1.readlines()


temp = Lines[0][:-1]
for i in range(len(temp)):
    if temp[i] == "R":
        instructions.append(1)
    else:
        instructions.append(0)

input_first = list()
input_second = list()
for i in range(2, len(Lines)):
    line = Lines[i]
    first = line.split(" = ")[0]
    second = [line[7:10], line[12:15]]
    input_first.append(first)
    input_second.append(second)
    #print(first)
    #print(second)

# search(0, input_first, input_second, "AAA")
# foo.sort(key=lambda i: (i[1], i[0]))

results = list()

# MXA VQA CBA JBA AAA HSA
for letter in ["MXA", "VQA", "CBA", "JBA", "AAA", "HSA"]:
    i = 0
    print(letter)
    while letter[2] != "Z":
        letter = input_second[input_first.index(letter)][instructions[i % len(instructions)]]
        i += 1
    results.append(i)
    print(i)
    print(letter)

# 13019

print(lcm(results[0], results[1], results[2], results[3], results[4], results[5]))

for letter in ["QMZ", "SHZ", "ZZZ", "XHZ", "KFZ", "FXZ"]:
    i = 1
    letter = input_second[input_first.index(letter)][instructions[i % len(instructions)]]
    while letter[2] != "Z":
        letter = input_second[input_first.index(letter)][instructions[i % len(instructions)]]
        i += 1
    results.append(i)
    print(i)
    print(letter)