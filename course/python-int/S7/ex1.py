def main():
    largura = int(input("Digite a largura: "))
    altura = int(input("Digite a altura: "))

    a = 0
    while (a < altura):
        l = 0
        while (l < largura):
            print("#", end="")
            l += 1
        a += 1
        print("")

main()
    