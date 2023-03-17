input = int(input("Por favor, digite um número: "))

ehPar = (input % 3 == 0)

if(ehPar):
    print("Fizz")
else:
    print(input)