import math

a = int(input("Por favor, digite o a: "))
b = int(input("Por favor, digite o b: "))
c = int(input("Por favor, digite o c: "))

delta = b**2 - 4* a * c

#print(delta)

if (delta < 0):
    print("esta equação não possui raízes reais")
    
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    if (delta == 0):
        print("a raiz desta equação é", raiz1)
    else:
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        
        if (raiz1 < raiz2):
            print("as raízes da equação são", raiz1, "e", raiz2)
        else:
            print("as raízes da equação são", raiz2, "e", raiz1)