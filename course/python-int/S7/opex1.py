def n_primos(n):
    x = 2
    numerosPrimos = 1

    while x < n:
        if ehPrimo(x):
            numerosPrimos += 1
        x += 1

    return numerosPrimos

def ehPrimo(n):
    ehPrimo = True

    if (n == 0 or n == 1 or n == 2):
        ehPrimo = False

    i = 2
    while (i < n):
        if (n % i == 0):
            ehPrimo = False
            break
        i += 1

    return ehPrimo

# def main():
#     while True:
#         n = int(input("Digite um numero: "))
#         print(n_primos(n))
# main()