import random
L = [random.randint(1, 100) for i in range(30)]
print(L)

def bubble(list):
    listlength = 0

    for e in list:
        listlength += 1

    for i in range(listlength):
        for j in range(0, listlength - i - 1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
bubble(L)
print(L)