def my_long_word(n, sentence):
    list = sentence.split(" ")
    print(list)
    mots = []
    for e in list:
        longueur = 0
        for u in e:
            longueur += 1
        for i in range(longueur):
            if i > n:
                mots.append(e)
                break
    print(mots)

my_long_word(2, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la "
                "colère mène à la haine, la haine mène à la souffrance")