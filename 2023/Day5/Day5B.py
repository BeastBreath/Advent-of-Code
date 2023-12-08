def convertToArray(Lines, start, end):
    start -= 1
    end -= 1
    retValue = list()
    for i in range(start, end + 1):
        retValue.append([0]*3)
        # Dest Origin # --> Origin # Dest 
        retValue[i - start][0] = int(Lines[i].split()[1])
        retValue[i - start][1] = int(Lines[i].split()[2])
        retValue[i - start][2] = int(Lines[i].split()[0])
    
    retValue.append([-1,0,0])
    retValue.sort(key=lambda x: x[0])
    return retValue

def pt2 (seeds, r):
    newSeeds = list()
    i = 0
    j = 0
    currentSeed = 0
    currentSeedNum = seeds[i] + currentSeed
    while currentSeed <= seeds[-1][0] + seeds[-1][1]:
        if currentSeed == seeds[i][1]:
            currentSeed = 0
            i += 1
        
        currentSeedNum = seeds[i] + currentSeed
        if currentSeedNum > r[j + 1][0]:
            j += 1
            continue
        
        if currentSeedNum < r[j]
    

file1 = open('input.txt', 'r')
Lines = file1.readlines()            

seeds = Lines[0].split()[1:]
for i in range(0, len(seeds)):
    seeds[i] = int(seeds[i])

seeds.sort()

# seed to soil
r = convertToArray(Lines, 4, 20)

numOfSeeds = len(seeds)
print(seeds)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)

# soil to fert
r = convertToArray(Lines, 23, 36)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)

# fert to water
r = convertToArray(Lines, 39, 69)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)

#water to light
r = convertToArray(Lines, 72, 89)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)

# light - temp
r = convertToArray(Lines, 92, 136)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)



#temperature-to-humidity map:
r = convertToArray(Lines, 139, 176)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)

#humidity-to-location map:
r = convertToArray(Lines, 179, 187)
for k in range(numOfSeeds):
    i = -1
    while i + 1 < len(r) and seeds[k] > r[i + 1][0]:
        i += 1
    print(i)
    print(seeds[k])
    if i == -1:
        print("K " + str(k))
        seeds[k] = seeds[k]
    elif r[i][0] + r[i][2] - 1 >= seeds[k]:
        print("K2 " + str(k))
        seeds[k] = r[i][1] + (seeds[k] - r[i][0])
    else:
        print("K3 " + str(k))
        seeds[k] = seeds[k]

print(seeds)
print(min(seeds))