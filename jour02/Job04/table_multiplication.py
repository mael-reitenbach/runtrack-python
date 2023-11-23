def selection_nb():
    print("Choisissez un nombre entier supérieur à 0 :")
    nb = input()
    try:
        int(nb)
    except:
        selection_nb()
    if int(nb) <= 0:
        selection_nb()
    else:
        print(f"{nb} x 1 = {nb}")
        print(f"{nb} x 2 = {int(nb)*2}")
        print(f"{nb} x 3 = {int(nb)*3}")
        print(f"{nb} x 4 = {int(nb)*4}")
        print(f"{nb} x 5 = {int(nb)*5}")
        print(f"{nb} x 6 = {int(nb)*6}")
        print(f"{nb} x 7 = {int(nb)*7}")
        print(f"{nb} x 8 = {int(nb)*8}")
        print(f"{nb} x 9 = {int(nb)*9}")
        print(f"{nb} x 10 = {int(nb)*10}")


selection_nb()