noms_produits = ["Oreille de nain", "Jambe de robots", "Poil de Mathis"]
prix = [2, 26, 971]
quantité = [78, 29, 2]
i = 0
print(i)

def selectionnement():
    print("Quel produit souhaitez vous acheter ? 1, 2 ou 3 ?")
    selection = int(input())
    
    if selection not in [1,2,3]:
        print("Choisissez 1, 2 ou 3")
        selectionnement()
    else:
        selection -= 1
        print(f"Combien de {noms_produits[selection]} voulez vous acheter ?")
        achat_quantite = int(input())
        if achat_quantite > quantité[selection]:
            print("On n'a pas assez de stock, veuillez en prendre moins.")
            selectionnement()
        else:
            quantité[selection] = quantité[selection]-achat_quantite
            shop()

def shop():
    global i
    print("Voici les produits disponibles :")
    for x in noms_produits:
        print(f"{i+1}) {x}")
        print("-")
        print(f"Prix : {prix[i]}$ | Quantité : {quantité[i]}")
        print("---")
        print("---")
        if i == len(noms_produits)-1:
            i = 0
            selectionnement()
        else:
            i += 1

def inflation():
    global quantité
    for x in quantité:
        print(f"prix avant l'inflation: {x}")
        x = round(x*1.1)
        print(f"prix après l'inflation: {x}")

shop()
inflation()