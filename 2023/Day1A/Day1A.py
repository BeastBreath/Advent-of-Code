
def findFirst(s):
    s: str
    for i in s:
        if i.isdigit():
            return int(i)
        
        
def findLast(s):
    s: str
    for i in reversed(s):
        if i.isdigit():
            return int(i)
        
        
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
sum = 0
# Strips the newline character
for line in Lines:
    sum += 10 * findFirst(line) + findLast(line)
    
print(sum)
    

        
        
    