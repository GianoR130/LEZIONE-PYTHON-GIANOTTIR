numero1 = int(input("Scrivi un numero: "))
if numero1 %3 == 0:
    if numero1 %5 == 0:
        print("il numero è divisibile sia per 3 che per 5.")
    else:
        print("Il numero è divisibile per 3.")
elif numero1 %5 == 0:
    print("Il numero è divisibile per 5.")