somma = 0
numero = int(input("Inserisci un numero (0 per terminare): "))
while numero != 0:
    somma += numero
    numero = int(input("Inserisci un altro numero (0 per terminare): "))
print("La somma complessiva dei numeri inseriti è:",somma)
