import random
minimo = int(input("Inserisci il valore minore(tra 0 e 100): "))
massimo = int(input("Inserisci il valore maggiore (tra 0 e 100): "))
if minimo < 0 or massimo > 100 or minimo >= massimo:
    print("I valori inseriti non sono validi. Il minimo deve essere inferiore al massimo e entrambi devono essere tra 0 e 100.")
else:
    numeri_validi = []
    conteggio = 0
    while len(numeri_validi) < 10:
        numero = random.randint(0, 100)
        conteggio += 1
        if minimo <= numero <= massimo:
            numeri_validi.append(numero)
    print(f"I numeri validi generati sono: {numeri_validi}")
    print(f"Totale numeri generati: {conteggio}")
