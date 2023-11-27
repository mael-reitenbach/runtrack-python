def Calcule(num1, operator, num2):
    if type(num1) != int:
        raise ValueError
    if type(num2) != int:
        raise ValueError 
    if type(operator) != str:
        raise ValueError
    if operator not in ["+","-","*","/","%"]:
        raise ValueError
    if operator == "+":
        print(num1+num2)
        return num1+num2
    if operator == "-":
        print(num1-num2)
        return num1-num2
    if operator == "*":
        print(num1*num2)
        return num1*num2
    if operator == "/":
        print(num1/num2)
        return num1/num2
    if operator == "%":
        print(num1%num2)
        return num1%num2


Calcule(3,"-",8)