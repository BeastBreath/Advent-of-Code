from collections import Counter


CON = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']



def checkline(s):
    mred = -1
    mgreen = -1
    mblue = -1
    game = (s.split(": "))[1].split("; ")
    for draw in game:
        draw = draw.split(", ")
        for set in draw:
            numberOfBalls = int((set.split())[0])
            color = (set.split())[1]
            if color == "red":
                mred = max(mred, numberOfBalls)
            elif color == "green":
                mgreen = max(mgreen, numberOfBalls)
            elif color == "blue":
                mblue = max(mblue, numberOfBalls)
    return mred * mgreen * mblue


file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
hands = list()
for line in Lines:
    print(line)
