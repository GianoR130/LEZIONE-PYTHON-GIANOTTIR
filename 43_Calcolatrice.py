n1 = float(input("Inserire il primo numero: "))
n2 = float(input("Inserire il secondo numero: "))
print("Scegliere tipologia di calcolo: Addizione(+) - Sottrazione(-) - Moltiplicazione(x) - Divisione(:)")
calc = input()
if calc == "+" or calc == "Addizione":
    risultato = n1 + n2
    print("Il risultato è:",risultato)

if calc == "-" or calc == "Sottrazione":
    risultato = n1 - n2
    print("Il risultato è:",risultato)

if calc == "x" or calc == "Moltiplicazione":
    risultato = n1 * n2
    print("Il risultato è:",risultato)

if calc == ":" or calc == "Divisione":
    risultato = n1 / n2
    print("Il risultato è:",risultato)