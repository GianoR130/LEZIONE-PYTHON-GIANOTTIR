giorno = int(input("Inserisci il giorno da 1-31: "))
if giorno > 31 or giorno < 1:
    print("Il giorno non è valido.")
    exit()
mese = int(input("Inserisci il mese solo della prima metà dell'anno: "))
if mese == 12 or mese == 1 or mese == 2:
    stagione = "Inverno"
    print("Il", giorno, "di", mese, "corrisponde alla stagione", stagione)
elif mese == 3 or mese == 4 or mese == 5:
    stagione = "Primavera"
    print("Giorno", giorno, "del mese", mese, "corrisponde alla stagione", stagione)
else:
    print("Mese oltre la prima metà dell'anno.")