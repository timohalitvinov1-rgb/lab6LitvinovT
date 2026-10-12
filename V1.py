from itertools import*
s = str(input("введи строку: "))
for i in permutations(s):
    print(i, end = "")
