def saison(type, time):
    type, time = type.lower(), time.lower()
    if type == "fruits":
        if time == "hiver":
            print("orange, mandarine et kiwi")
        elif time == "ete":
            print("poire, fraise, cassis")
    elif type == "legumes":
        if time == "hiver":
            print("carotte, topinambour, endive")
        elif time == "ete":
            print("artichaut, aubergine, navet")
    else:
        print("Donne une saison valide")

saison("fruits", "hiver")
saison("legumes", "ete")
saison("sdq", "sqdgsq")