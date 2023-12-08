from collections import Counter


CON = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']



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
    prehand = line.split()[0]
    bid = line.split()[1]
    hand = list()
    for card in prehand:
        hand.append(CON.index(card))
        
    res = list(Counter(hand).values())
    res.sort(reverse=True)
    print(res)
    
    type = 0 #5 of a kind, 4 of a kind, 3/2, 3, 2 2, 1
    if res[0] == 5:
        type = 6
    elif res[0] == 4:
        type = 5
    elif res[0] == 3 and res[1] == 2:
        type = 4
    elif res[0] == 3:
        type = 3
    elif res[0] == 2 and res[1] == 2:
        type = 2
    elif res[0] == 2:
        type = 1
    elif res[0] == 1:
        type = 0
    else:
        print("HELPP")
        
    print(type)
    
    hands.append([type, hand, int(bid)])
    
hands.sort(key=lambda i: (i[0], i[1][0],  i[1][1],  i[1][2],  i[1][3],  i[1][4]), reverse=True)

print(hands)

sum = 0
for i in range(len(hands)):
    sum += (len(hands) - i) * hands[i][2]

print(sum)
# foo.sort(key=lambda i: (i[1], i[0]))
