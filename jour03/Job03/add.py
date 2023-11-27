def Add(a,b):
    if type(a) != int:
        raise ValueError
    if type(b) != int:
        raise ValueError    
    print(a+b)

Add(3,5)
Add(4,7.4)
Add(8,"wddvsf")

