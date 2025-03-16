import random
n = int(input("Inserire un numero: "))
somma_positiva = 0
somma_negativa = 0
casuali = [random.randint(-20,20) for i in range(n)]
for num in casuali:
    if num > 0:
        somma_positiva += num
    elif num < 0:
        somma_negativa += num
print("Somma positiva:",somma_positiva)
print("Somma negativa:",somma_negativa)