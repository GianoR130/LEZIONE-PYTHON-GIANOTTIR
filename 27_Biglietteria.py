prezzo = float(input("Inserisci il prezzo del biglietto: "))
numero = int(input("Inserisci il numero di biglietti acquistati: "))
omaggio = numero // 20
totale_biglietti = numero - omaggio
totale = totale_biglietti * prezzo
print("Il totale da pagare è:", totale)
