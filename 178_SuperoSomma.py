import random
listanum = [random.randint(1, 10) for i in range(20)]
n = int(input("Inserisci un numero: "))
print("Lista generata:", listanum)
somma = 0
conteggio = 0
for num in listanum:
    somma += num
    conteggio += 1
    if somma >= n:
        break
if somma >= n:
    print("Servono",conteggio,"elementi per raggiungere almeno",n)
else:
    print("La somma di tutti gli elementi non raggiunge il valore indicato.")