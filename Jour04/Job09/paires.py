L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
c = 0
for i in L:
    if (i % 2 == 0):
        c += i
    if i == 91:
        print(c)
