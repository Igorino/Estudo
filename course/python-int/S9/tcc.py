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
    top = 0
    for i in range(len(as_a)):
        top += abs(as_a[i] - as_b[i])
    resultado = top / len(as_a)
    
    return resultado

'''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
def calcula_assinatura(texto):
    '''
        Assinatura: 
        - Tamanho medio da palavra: media simples do numero de char p/ palavra
        - Relacao Type-Token: num. de palavras diferentes div. pelo total
        - Razao Hapax Legomana: num. de palavras unicas div. pelo total
        - Tamanho medio de sentenca: media simples do num. de char por sentenca
        - Complexidade da sentenca: media simples do numero de frases por sentenca
        - Tamanho medio da frase: media simples do num. de chars por frase
    '''
    soma_tamanhos_das_palavras = 0
    num_de_palavras = 0

    '''todas_as_palavras_lista = separa_palavras(separa_frases(separa_sentencas(texto)))'''
    todas_as_palavras_lista = pega_lista_total_de_palavras(texto)
    num_de_palavras = len(todas_as_palavras_lista)
    for palavra in todas_as_palavras_lista:
        soma_tamanhos_das_palavras = soma_tamanhos_das_palavras + len(palavra)
    
    num_carateres_sentencas = 0
    lista_de_sentencas = separa_sentencas(texto)
    num_de_sentencas = len(lista_de_sentencas)
    for sentenca in lista_de_sentencas:
        num_carateres_sentencas = num_carateres_sentencas + len(sentenca)

    num_carateres_frase = 0
    lista_de_frases = pega_lista_total_de_frases(texto)
    num_de_frases = len(lista_de_frases)
    for frase in lista_de_frases:
        num_carateres_frase = num_carateres_frase + len(frase)

    n_palavras_dif = n_palavras_diferentes(todas_as_palavras_lista)
    n_palavras_uni = n_palavras_unicas(todas_as_palavras_lista)

    tam_medio_palavra = soma_tamanhos_das_palavras / num_de_palavras
    relacao_type_token = n_palavras_dif / num_de_palavras
    relacao_hapax_legomana = n_palavras_uni / num_de_palavras
    tam_medio_sentenca = num_carateres_sentencas / num_de_sentencas
    complex_de_sentenca = num_de_frases / num_de_sentencas
    tam_medio_frase = num_carateres_frase / num_de_frases

    assinatura = [tam_medio_palavra, relacao_type_token, relacao_hapax_legomana, tam_medio_sentenca, complex_de_sentenca, tam_medio_frase]

    return assinatura

def pega_lista_total_de_frases(texto):
    frases_total = []
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        frases_total = frases_total + frases
    
    return frases_total

def pega_lista_total_de_palavras(texto):
    palavras_total = []
    sentencas = separa_sentencas(texto)
    for sentenca in sentencas:
        frases = separa_frases(sentenca)
        for frase in frases:
            palavras = separa_palavras(frase)
            palavras_total = palavras_total + palavras
    
    return palavras_total

'''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
def avalia_textos(textos, ass_cp):
    numero_do_texto_atual = 1
    numero_do_texto_infectado = numero_do_texto_atual
    menor_assinatura = compara_assinatura(calcula_assinatura(textos[0]), ass_cp)
    assinatura = 0
    for texto in textos:
        assinatura = compara_assinatura(calcula_assinatura(texto), ass_cp)
        if assinatura < menor_assinatura:
            menor_assinatura = assinatura
            numero_do_texto_infectado = numero_do_texto_atual
        numero_do_texto_atual += 1

    return numero_do_texto_infectado

'''
def main():
    #texto = "Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova."
    #print(calcula_assinatura(texto))
    assinatura_exemplo = le_assinatura()
    textos = le_textos()
    print("O autor do texto", avalia_textos(textos, assinatura_exemplo) ,"está infectado com COH-PIAH")

main()
'''