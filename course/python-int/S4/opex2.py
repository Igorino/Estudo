numero = int(input("Digite um número inteiro: "))

temRepeticao = False

while(numero > 0):
    ultimaCasa = numero % 10
    numero = numero // 10 
    proxCasa = numero % 10
    if (ultimaCasa == proxCasa):
        temRepeticao = True

if (temRepeticao):
    print("sim")
else:
    print("não")