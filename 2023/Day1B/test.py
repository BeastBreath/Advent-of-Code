s = "Game 1: 4 red, 5 blue, 4 green; 7 red, 8 blue, 2 green; 9 blue, 6 red; 1 green, 3 red, 7 blue; 3 green, 7 red"


s = s[8:].split("; ")

s = s[1].split(', ')

print(s)