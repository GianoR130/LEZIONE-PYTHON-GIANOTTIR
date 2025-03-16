import random
n = int(input("Inserire la quantità nella lista: "))
pari = 0
dispari = 0
lista = [random.randint(1,20) for i in range(n)]
for num in lista:
    if num % 2 == 0:
        pari += 1
    if num % 2 != 0:
        dispari += 1
print("Lista generata:",lista)
print("Quantità pari:",pari)
print("Quantità dispari:",dispari)