def colonne(n):
    tapstring = f"+{'-'*(n+1)}+\n"
    for i in range(n+2):
        if i is not n+1:
            tapstring += f"|{'#'*(n-i)+' '+'#'*(i)}|\n"
        else:
            tapstring += f"+{'-'*(n+1)}+"
    print(tapstring)

colonne(10)
colonne(34)