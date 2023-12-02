def checkline(s):
    game = (s.split(": "))[1].split("; ")
    for draw in game:
        draw = draw.split(", ")
        for set in draw:
            numberOfBalls = int((set.split())[0])
            color = (set.split())[1]
            if color == "red" and numberOfBalls > 12:
                return False
            elif color == "green" and numberOfBalls > 13:
                return False
            elif color == "blue" and numberOfBalls > 14:
                return False
    return True


file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
sum = 0
i = 0
for game in Lines:
    i += 1
    if(checkline(game)):
        sum += i
            

print(sum)