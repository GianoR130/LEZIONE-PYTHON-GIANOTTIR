import time
pupazzo = 14.90
macchina = 1.50
carta = 4.50
print("Pupazzo € 14.90")
print("Macchinina € 1.50")
print("Carta € 4.50")
n1 = int(input("Inserire la quantità di pupazzi (scrivere 0 se non voluti): "))
n2 = int(input("Inserire la quantità di macchinine (scrivere 0 se non volute): "))
n3 = int(input("Inserire la quantità di pacchetti pokemon (scrivere 0 se non voluti): "))
articoli = n1 + n2 + n3
prezzo = (pupazzo * n1) + (macchina * n2) + (carta * n3)
print("Totale articoli:",articoli)
print("Totale prezzo senza sconto:",prezzo)
print("Calcolo sconto...")
time.sleep(1.5)
if articoli < 10:
    if prezzo >= 10:
        prezzo_scontato = prezzo * 0.95
    elif prezzo < 10:
        prezzo_scontato = prezzo * 0.98
elif articoli == 10:
    prezzo_scontato = prezzo * 0.90
elif articoli > 10:
    if prezzo > 100:
        prezzo_scontato = prezzo * 0.50
    elif prezzo < 100:
        prezzo_scontato = prezzo * 0.70
print("Il totale scontato è:",prezzo_scontato)

    


