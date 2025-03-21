import random
listanum = [random.randint(1,100) for i in range(20)]
n = int(input("Inserisci un numero: "))
listapari = [num for num in listanum if num % 2 == 0][:n]
print()
print("Lista originale:", listanum)
print("Lista dei primi",n, "numeri pari:", listapari)