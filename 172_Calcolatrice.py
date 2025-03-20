risposta = ""
while risposta != "no":
    num1 = float(input("Inserire il primo numero: "))
    num2 = float(input("Inserire il secondo numero: "))
    operazione = input("Scegliere l'operazione (+, -, *, /): ")
    if operazione == "+":
        print("Risultato:",num1+num2)
    elif operazione == "-":
        print("Risultato:",num1-num2)
    elif operazione == "*":
        print("Risultato:",num1*num2)
    elif operazione == "/":
            if num2 == 0:
                 print("Errore: Divisione per zero")
            else:
                print("Risultato:",num1/num2)
    if input("Vuoi continuare? (si/no): ").strip().lower() == 'no':
            break