stringa = "Esempio di stringa"
posizione = int(input("Inserisci una posizione: "))
if 0 <= posizione <= len(stringa):
    print("Caratteri prima della posizione:", stringa[:posizione])
else:
    print("Posizione non valida!")
    