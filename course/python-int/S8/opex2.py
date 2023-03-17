def le_sequencia():
    sequencia = []
    item = -1
    while item != 0:
        item = int(input("Digite um número: "))
        if item != 0:
            sequencia.append(item)
            
    return sequencia

def inverte_sequencia(sequencia):
    sequenciaInvertida = []
    for item in sequencia:
        sequenciaInvertida.insert (0, item)
    return sequenciaInvertida

def imprime_sequencia(sequencia):
    for item in sequencia:
        print(item)

def main():
    sequencia = le_sequencia()
    sequencia = inverte_sequencia(sequencia)
    imprime_sequencia(sequencia)

main()