def linePoints(s):
    s: str
    s = (s.split(": "))[1]
    winning_numbers = s.split(" | ")[0].split()
    your_numbers = s.split(" | ")[1].split()
    count = 0
    for number in your_numbers:
        if number in winning_numbers:
            count += 1
    return count





file1 = open('input.txt', 'r')
Lines = file1.readlines()

countOfCards = [1] * 220
i = 0
for line in Lines:
    n = linePoints(line)
    for k in range (i+1,i+n+1):
        if k <= 220:
            countOfCards[k] += countOfCards[i]
    i += 1
            

print(sum(countOfCards))