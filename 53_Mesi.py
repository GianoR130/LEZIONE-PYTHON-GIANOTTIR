mese = int(input("Inserire il numero del mese: "))
if mese == 1 or mese == 3 or mese == 5 or mese == 7 or mese == 8 or mese == 10 or mese == 12:
    print("Il numero di giorni sono 31")
elif mese == 4 or mese == 6 or mese == 9 or mese == 11:
    print("Il numero di giorno sono 30")
else:
    print("Il numero di giorni sono 28 o 29 negli anni bisestili")