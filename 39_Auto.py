prezzo = float(input("Inserisci il prezzo dell'automobile: "))
if prezzo > 20000:
    prezzo = prezzo * 0.9
    contanti = input("Vuoi pagare in contanti? Si o no: ")
    if contanti == "Si":
        prezzo = prezzo - 1000
elif prezzo > 10000 and prezzo < 20000:
    prezzo = prezzo * 0.95
    contanti = input("Vuoi pagare in contanti? Si o no: ")
    if contanti == "Si":
        prezzo = prezzo - 200
print("Devi pagare",prezzo)