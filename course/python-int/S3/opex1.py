import math

x1 = int(input("Por favor, digite o X do primeiro ponto: "))
y1 = int(input("Por favor, digite o Y do primeiro ponto: "))

x2 = int(input("Por favor, digite o X do segundo ponto: "))
y2 = int(input("Por favor, digite o Y do segundo ponto: "))


distancia = math.sqrt( ((x1 - x2)**2) + ((y1 - y2)**2) )

if(distancia >= 10):
    print("longe")
else:
    print("perto")