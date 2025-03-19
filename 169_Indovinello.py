import random
numero = random.randint(1,100)
risposta = ""
while risposta != "no":
    n = int(input("Indovinare un numero casuale da 1 a 100: "))
    if n > numero:
        print("Non hai indovinato,",n,"è maggiore del numero da indovinare!")
        risposta = input("Vuoi riprovare? ")
        
    if n < numero:
        print("Non hai indovinato,",n,"è minore del numero da indovinare!")
        risposta = input("Vuoi riprovare? ")
    
    if n == numero:
        print("Hai indovinato il numero!")
        risposta = input("Vuoi riprovare? ")
        numero = random.randint(1,100)