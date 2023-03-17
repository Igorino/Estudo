n = 1
while (n >= 0):
    n = int(input("Digite o valor de n: "))
    i = n

    if (n!=0):
        while (i > 1):
            i -= 1
            n = n*i
        print(n)
    else: 
        print("1")
    