prim = int(input("Por favor, digite o primeiro número: "))
seg = int(input("Por favor, digite o segundo número: "))
terc = int(input("Por favor, digite o terceiro número: "))

ehCescente = (prim <= seg <= terc)

if(ehCescente):
    print("crescente")
else:
    print("não está em ordem crescente")