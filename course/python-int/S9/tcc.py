import re

'''Essa funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

'''Essa funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

'''Essa funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

'''Essa funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

'''Essa funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
def separa_palavras(frase):
    return frase.split()

'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

'''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

'''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
def compara_assinatura(as_a, as_b):

    pass

'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
def calcula_assinatura(texto):

    pass

'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
def avalia_textos(textos, ass_cp):
    pass