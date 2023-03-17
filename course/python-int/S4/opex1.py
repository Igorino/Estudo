n = int(input("Digite aqui o número para ver se ele é primo: "))

ehPrimo = True

if (n == 0 or n == 1 or n == 2):
    ehPrimo = False

i = 2
while (i < n):
    if (n % i == 0):
        ehPrimo = False
        break
    i += 1

if (ehPrimo):
    print("primo")
else:
    print("não primo")