print("Benvenuto nel mio programma di conversazione.")
print()
risposta = input("Ti piace andare in bicicletta? Rispondi si o no: ")
if risposta == "Si":
    print("Molto bene! Ti terrai in forma!")
    risposta2 = input("Ti piace anche il basket?")
    if risposta2 == "Si":
        print("Allora sei una atleta!")
    else:
        print("Uno sport è meglio di niente!")
else:
    risposta3 = input("Ti piace il calcio? ")
    if risposta3 == "Si":
        print("Molto bene, ti terrai in forma!")

    else:
        print("Non tutti sono sportivi.")
    