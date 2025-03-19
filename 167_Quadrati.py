numero = 1
risposta = ""
while risposta != "no":
    print("Il quadrato di",numero,"è",numero**2)
    risposta = input("Vuoi continuare? ")
    if risposta != "no":
        numero += 1
