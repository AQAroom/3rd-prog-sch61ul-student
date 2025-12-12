a = int(input())
z = input()
b = int(input())
if z == "+":
    print(a +  b)
elif z == "-":
    print(a - b)
elif z == "*":
    print(a * b)
elif z == "/":
    print(a / b)
elif z == "^":
    print(a ** b)
else:
    print( "Неизвестная операция" )
