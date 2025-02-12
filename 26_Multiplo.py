numero1 = int(input("Inserisci il primo numero intero: "))
numero2= int(input("Inserisci il secondo numero intero: "))
if numero1 > numero2:
    if numero1 % numero2 == 0:
        print("Il numero va bene")
    elif numero1 % numero2 != 0:
        print("Il numero non va bene")
elif numero1 < numero2:
    if numero2 % numero1 == 0:
        print("Il numero va bene")
    elif numero1 % numero2 != 0:
        print("Il numero non va bene")