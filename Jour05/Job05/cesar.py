def cesar(phrase, code):
    crypt = ""
    for e in phrase:
        if ord(e) == 32:
            crypt+="a"
        else:
            crypt += chr((ord(e)+(ord(code)-96))%123)
    print(crypt)

cesar("Exterminer", "b")