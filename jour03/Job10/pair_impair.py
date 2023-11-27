def pair_impair(nombre):
    if type(nombre) is not int:
        return "Il faut un nombre entier"
    if nombre % 2 == 0:
        return "Pair"
    else:
        return "Impair"

print(pair_impair(11))
print(pair_impair(6))
print(pair_impair(7.1))
print(pair_impair(5))