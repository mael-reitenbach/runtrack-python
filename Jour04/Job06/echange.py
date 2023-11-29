import random

L = []
for i in range(0,random.randint(5, 27)):
    L.append(random.randint(0, 100))

print(L)
stk = L[len(L)-1]
L[len(L)-1] = L[0]
L[0] = stk
print(L)