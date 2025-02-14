import random
num1 = random.randint(0,10)
num2 = random.randint(0,10)
totale = num1 * num2
if totale > 20:
    differenza = num1 - num2
    print("La differenza è: ",differenza)
elif totale < 20:
    somma = num1 + num2
    print("La somma è: ",somma)
