numero = int(input("Digite um número inteiro: "))
resultado = 0

while(numero > 0):
    ultimaCasa = numero % 10
    numero = numero // 10 
    resultado += ultimaCasa

print(resultado)