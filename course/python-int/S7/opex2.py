import math

def soma_hipotenusas(h):
    hipotenusas = []
    resultado = 0
    a = 1
    b = 2
    while a**2 + b**2 <= h**2:
        h2 = a**2 + b**2
        maiorQueH2 = a**2 + b**2 <= h**2
        while (b > a):
            hipotenusaAtual = math.sqrt(a**2 + b**2)
            if (hipotenusaAtual % 1 == 0 and hipotenusaAtual <= h):
                if hipotenusaAtual not in hipotenusas:
                    hipotenusas.append(hipotenusaAtual)
            if (hipotenusaAtual == h):
                return soma(hipotenusas)
            a += 1
        a = 1
        b += 1
        
    return soma(hipotenusas)

def soma(hipotenusas):
    resultado = 0
    for hipotenusa in hipotenusas:
        resultado += hipotenusa
    return resultado

# def main():
#     while True:
#         numero = int(input("Digite um numero: "))
#         print(soma_hipotenusas(numero))
# main()