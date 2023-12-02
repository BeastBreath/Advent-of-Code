
nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]   
reverseNums = []
for i in nums:
    reverseNums.append(i[::-1])
   


def findFirst(s):
    if s[0].isdigit():
        return int(s[0])
    for n in range(10):
        if len(s) >= len(nums[n]) and s[0:len(nums[n])] == nums[n]:
            return n
    return findFirst(s[1:])
        
        
        
def findLast(s):
    if s[0].isdigit():
        return int(s[0])
    for n in range(10):
        if len(s) >= len(reverseNums[n]) and s[0:len(reverseNums[n])] == reverseNums[n]:
            return n
    return findLast(s[1:])
   
           
file1 = open('input.txt', 'r')
Lines = file1.readlines()
 
sum = 0
for line in Lines:
    sum += 10 * findFirst(line) + findLast(line[::-1])
    

print(sum)