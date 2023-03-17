def main():
    largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))

    a = 0
    while (a < altura):
        l = 0
        while (l < largura):
            if (l == 0 or l == largura-1 or a == 0 or a == altura-1):
                print("#", end="")
            else:
                print(" ", end="")
            l += 1
        a += 1
        print("")

main()
    