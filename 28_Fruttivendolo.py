quantita = int(input("Inserire la quantità delle pesche: "))
prezzo = 1.50
prezzo_totale = prezzo * quantita
if prezzo_totale > 10:
    print("Il prezzo totale è: ",prezzo_totale)
    prezzo_totale -= 0.20 * prezzo_totale
    print("Il prezzo scontato è: ",prezzo_totale)
else:
    print("Totale: ",prezzo_totale)