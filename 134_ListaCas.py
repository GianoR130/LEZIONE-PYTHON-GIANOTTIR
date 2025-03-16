import random
numeri_casuali = [random.randint(1, 100) for _ in range(10)]
print("Dalla prima all'ultima posizione:", numeri_casuali)
print("Dall'ultima alla prima posizione:", numeri_casuali[::-1])