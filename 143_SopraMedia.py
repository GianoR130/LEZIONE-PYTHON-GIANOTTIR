import random
casuali = [random.randint(1, 10) for _ in range(10)]
media = sum(casuali) / len(casuali)
numeri_superiori = [num for num in casuali if num > media]
print("Lista generata:",casuali)
print("Media della lista:", media)
print("Numeri superiori alla media:", numeri_superiori)
