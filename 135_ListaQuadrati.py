import random
n = int(input("Inserire un numero: "))
numero = [random.randint(1, 20) for i in range(n)]
print("Numeri generati:", numero)
numero_elevato = [num**2 for num in numero]
print("Numeri elevati al quadrato:", numero_elevato)
