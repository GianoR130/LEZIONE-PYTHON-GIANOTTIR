import random
nome = input("Inserisci il tuo nome: ")
numero = random.randint(0,99)
posizione = len(nome) // 2
password = nome[:posizione] + str(numero) + nome[posizione:]
print("La tua password generata è:", password)
