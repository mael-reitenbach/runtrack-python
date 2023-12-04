def draw_rectangle(largeur, hauteur):
    rectstring = ""
    if hauteur != 0:
        for i in range(hauteur):
            if i == 0:
                rectstring += f"|{'-'*int(largeur - 2)}|\n"
            elif i == hauteur - 1:
                rectstring += f"|{'-'*int(largeur - 2)}|"
            else:
                rectstring += f"|{' '*int(largeur - 2)}|\n"
    else:
        rectstring = f"|{'='*int(largeur - 2)}|"
    print(rectstring)

draw_rectangle(10, 3)
draw_rectangle(4, 0)
draw_rectangle(0, 5)
draw_rectangle(20, 5)