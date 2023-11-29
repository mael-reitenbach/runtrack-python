L = [10,20,30,20,10,50,60,40,80,50,40]

def bubble(list):
    listlength = 0
    for e in list:
        listlength += 1
    for i in range(listlength):
        for j in range(0, listlength - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
bubble(L)

listlength = 0
for e in L:
    listlength += 1
    for i in range(listlength):
        for j in range(0, listlength - i - 1):
            if L[j] == L[j+1]:
                del L[j]
print(L)