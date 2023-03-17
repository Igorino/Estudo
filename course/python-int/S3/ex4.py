input = int(input("Por favor, digite um número: "))

ehPar = (input % 5 == 0) and (input % 3 == 0)

if(ehPar):
    print("FizzBuzz")
else:
    print(input)