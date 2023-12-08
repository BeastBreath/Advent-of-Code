from collections import Counter


CON = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
hands = list()
for line in Lines:
    prehand = line.split()[0]
    bid = line.split()[1]
    hand = list()
    for card in prehand:
        hand.append(CON.index(card))
    
    joker_count = Counter(hand)[0]
    hand_no_joker = hand.copy()
    c = hand_no_joker.count(0) 
    for i in range(c): 
        hand_no_joker.remove(0) 
        
    res = list(Counter(hand_no_joker).values())
    print(res)
    print(list(Counter(hand).values()))
    res.sort(reverse=True)
    print(res)
    
    type = 0 #5 of a kind, 4 of a kind, 3/2, 3, 2 2, 1
    
    if joker_count == 5 or ((res[0] + joker_count) == 5):
        type = 6
    elif (res[0] + joker_count) == 4:
        type = 5
    elif (res[0] == 3 and res[1] == 2) or (res[0] == 2 and res[1] == 2 and joker_count == 1):
        type = 4
    elif (res[0] + joker_count) == 3:
        type = 3
    elif res[0] == 2 and res[1] == 2:
        type = 2
    elif (res[0] + joker_count) == 2:
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
