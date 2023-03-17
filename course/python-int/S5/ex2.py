def maior_primo(x):
    
    while (x > 1):
        if ehPrimo(x):
            return x
        x -= 1
    

    
def ehPrimo(n):
    ehPrimo = True

    if (n == 0 or n == 1 or n == 2):
        ehPrimo = False

    i = 2
    while (i < n):
        if (n % i == 0):
            ehPrimo = False
            break
        i += 1

    return ehPrimo