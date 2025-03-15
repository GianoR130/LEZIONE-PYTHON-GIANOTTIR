n = int(input("Inserisci un numero intero n: "))
for i in range(1, int(n**(1/3)) + 1):
    cubo = i**3
    if cubo <= n:
        print(cubo, end=" ")