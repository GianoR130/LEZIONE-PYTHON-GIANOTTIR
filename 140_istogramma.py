import random
n = int(input("Inserire la quantità nella lista: "))
lista = [random.randint(1,15) for i in range(n)]
for num in lista:
    print("*" * num)
    print()
print("Lista:",lista)