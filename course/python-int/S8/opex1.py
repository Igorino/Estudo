def maior_elemento(lista):
    maior = lista[0]
    for item in lista:
        if item > maior:
            maior = item
    return maior

def main():
    print(maior_elemento([1,4,2,5,7,3,9,12,5,2]))

main()