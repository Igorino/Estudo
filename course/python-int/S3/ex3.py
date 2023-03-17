input = int(input("Por favor, digite um número: "))

ehPar = (input % 5 == 0)

if(ehPar):
    print("Buzz")
else:
    print(input)