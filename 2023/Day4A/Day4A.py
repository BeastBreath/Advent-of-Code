def linePoints(s):
    s: str
    s = (s.split(": "))[1]
    winning_numbers = s.split(" | ")[0].split()
    your_numbers = s.split(" | ")[1].split()
    count = 0
    for number in your_numbers:
        if number in winning_numbers:
            count += 1
    if count == 0:
        return 0
    return 2 ** (count - 1)





file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
sum = 0
for line in Lines:
    sum += linePoints(line)    

print(sum)