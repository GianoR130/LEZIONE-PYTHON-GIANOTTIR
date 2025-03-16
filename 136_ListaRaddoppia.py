import random
cas = [random.randint(1, 50) for i in range(10)]
modificati = [num * 2 if num % 2 != 0 else num for num in cas]
print("Lista originale:", cas)
print("Lista raddoppiata:", modificati)
