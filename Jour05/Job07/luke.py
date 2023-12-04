from random import *
def luke(notes):
    for i in range(len(notes)):
        if notes[i] < 40:
            notes[i] = f"{notes[i]} échoué"
        elif notes[i]%5 >= 3:
                notes[i] = 5*(notes[i] // 5) + 5
    return(notes)

randomnotes = [randint(0, 100) for i in range(20)]
print(randomnotes)
print(luke(randomnotes))