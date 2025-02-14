quantita = int(input("Inserire i litri di benzina necessaria: "))
prezzo = 1.76
prezzo_totale = prezzo * quantita
if prezzo_totale > 60:
    print("Il prezzo totale è: ",prezzo_totale)
    prezzo_totale -= 0.05 * prezzo_totale
    print("Il prezzo scontato è: ",prezzo_totale)
else:
    print("Totale: ",prezzo_totale)