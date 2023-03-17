def remove_repetidos(lista):
    lista.sort()
    listaNova = []
    anterior = 0

    for x in range(len(lista)):
        item = lista[x]
        if item != anterior:
            listaNova.append(lista[x])
        anterior = item
        
    return listaNova

# [1, 2, 3, 3, 4, 5]

# def main():
#     print(remove_repitidos([1, 2, 3, 3, 4, 4, 4, 4, 5, 5]))
#     print(remove_repitidos([5,5,5,1,4,5,2,3,2,3,1,5]))

# main()