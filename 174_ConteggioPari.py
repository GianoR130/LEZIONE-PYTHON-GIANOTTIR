import random
n = int(input("Inserisci un numero intero: "))
generati = []
pari = 0
while pari < n:
    numero = random.randint(40, 90)
    generati.append(numero)
    print("Generato:",numero)
    if numero % 2 == 0:
        pari += 1
    
print("Numeri totali generati:",len(generati))
