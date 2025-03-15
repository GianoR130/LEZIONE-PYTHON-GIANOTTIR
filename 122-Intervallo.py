a = int(input("Inserire il numero a: "))
b = int(input("Inserire il numero b: "))
somma = 0
if a < b:
    for i in range(a,b+1):
        print(i)
        somma += i
    print("Somma:",somma)
elif a > b:
    print("Errore, il numero 'a' deve essere maggiore di 'b'")