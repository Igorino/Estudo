def computador_escolhe_jogada(n, m):
    numeroDePecasRetiradas = 1

    for numeroDePecasRetiradas in range(1, m+1):
        if ((n - numeroDePecasRetiradas) % (m+1) == 0):
            break

    if (numeroDePecasRetiradas == 1):
        print("O computador tirou uma peça.")
    else:
        print("O computador tirou", numeroDePecasRetiradas,"peças.")

    return numeroDePecasRetiradas

def usuario_escolhe_jogada(n, m):
    while (True):
        numeroDePecasRetiradas = int(input("Quantas peças você vai tirar? "))
        if(numeroDePecasRetiradas < 1 or numeroDePecasRetiradas > n or numeroDePecasRetiradas > m):
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
        else:
            break

    if (numeroDePecasRetiradas == 1):
        print("Você tirou uma peça.")
    else:
        print("Você tirou", numeroDePecasRetiradas,"peças.")


    return numeroDePecasRetiradas

def partida():
    jogadorGanhou = True

    print()
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()

    voceComeca = (n % (m+1) == 0)
    if voceComeca:
        print("Você começa!")
        while(n > 0):
            n -= usuario_escolhe_jogada(n, m)
            if (n == 0):
                jogadorGanhou = True
                print("Fim do jogo! Você ganhou!")
                break
            else:
                pecasRestantes(n)

            n -= computador_escolhe_jogada(n, m)
            if (n == 0):
                jogadorGanhou = False
                print("Fim do jogo! O computador ganhou!")
                break
            else:
                pecasRestantes(n)
    else:
        print("Computador começa!")
        while(n > 0):
            n -= computador_escolhe_jogada(n, m)
            if (n == 0):
                jogadorGanhou = False
                print("Fim do jogo! O computador ganhou!")
                break
            else:
                pecasRestantes(n)

            n -= usuario_escolhe_jogada(n, m)
            if (n == 0):
                jogadorGanhou = True
                print("Fim do jogo! Você ganhou!")
                break
            else:
                pecasRestantes(n)
    print()
    return jogadorGanhou

def pecasRestantes(n):
    if (n == 1):
        print("Agora resta apenas uma peça no tabuleiro.")
    elif (n > 1):
        print("Agora restam", n, "peças no tabuleiro.")
    print()

def campeonato():
    vitoriasJogador = 0
    vitoriasComputador = 0
    for i in range(3):
        print("***** Rodada", i+1, "*****")
        jogadorGanhou = partida()
        if jogadorGanhou:
            vitoriasJogador += 1
        else:
            vitoriasComputador += 1
    print()
    print("***** Final do campeonato! *****")
    print()
    print("Placar: Você ", vitoriasJogador," X ", vitoriasComputador," Computador")


def main():
    print("Bem-vindo ao jogo do NIM! Selecione:")
    print()
    print("1 - para jogar uma partida isolada")
    print("2 - para jogar um campeonato")
    print()
    escolha = input("Escolha: ")

    if escolha == "1":
        print()
        print("Você escolheu uma partida!")
        print()
        partida()
    elif escolha == "2":
        print()
        print("Você escolheu um campeonato!")
        print()
        campeonato()
    else:
        print("Escolha inválida!")    

main()
