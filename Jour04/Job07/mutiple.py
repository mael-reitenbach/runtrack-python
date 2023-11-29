L = [8, 24,48,2,16]
c = 0
for i in L:
    if (i % 3 == 0):
        c += 1
    if i == 16:
        print(c)
