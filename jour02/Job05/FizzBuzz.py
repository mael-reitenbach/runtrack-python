for x in range(1,101):
    a = ""
    b = ""
    if x % 3 == 0:
        a = "Fizz"
    if x % 5 == 0:
        b = "Buzz"
    if len(a+b) > 3:
        print(f"{a}{b}")
    else:
        print(x)