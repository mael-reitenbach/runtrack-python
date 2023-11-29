import random

L = []
for i in range(0,5):
    L.append(random.randint(0, 100))

print(L)

print(L[1])

def remplace():
    n = L[2] + L[4]
    L[3] = n
    print(L)
    print(L[4])

remplace()