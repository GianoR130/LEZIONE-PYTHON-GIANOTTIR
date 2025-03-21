import random
listanum = [random.randint(1,100) for i in range (20)]
n = int(input("Inserire un numero da cercare: "))
print("Lista originale:", listanum)
count = 0
for q in listanum:
    if q == n:
        break
    count += 1
if count == len(listanum):
    print("Il numero",n,"non è presente nella lista.")
else:
    print("Il numero",n,"si trovo dopo",count,"elementi.")