L = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

rond = [int(e) for e in L]
print(rond)

listlength = 0
for e in rond:
    listlength += 1
for i in range(listlength):
    for j in range(0, listlength - i - 1):
        if rond[j] > rond[j+1]:
            rond[j], rond[j+1] = rond[j+1], rond[j]

print(rond)