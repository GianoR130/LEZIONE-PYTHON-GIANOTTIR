import random
n = int(input("Inserire un numero: "))
casuali = [random.randint(1,20) for i in range(n)]
somma = sum(casuali)
print("Numeri casuali:",casuali)
print("Somma numeri casuali:",somma)