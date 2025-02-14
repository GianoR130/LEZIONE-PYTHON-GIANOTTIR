numero1 = int(input("Inserire il primo numero: "))
numero2 = int(input("Inserire il secondo numero: "))
if numero1 > numero2:
    risultato = numero1 - numero2
    print("Il risultato è",numero1,"-",numero2,"=",risultato)
else:
    risultato = numero2 - numero1
    print("Il risultato è",numero2,"-",numero1,"=",risultato)
