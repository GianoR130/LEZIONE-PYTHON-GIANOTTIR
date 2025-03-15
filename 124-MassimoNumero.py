n = int(input("Quanti numeri compongono la sequenza? "))
massimo = None
for i in range(n):
    numero = int(input(f"Inserisci il numero {i+1}: "))
    if massimo is None or numero > massimo:
        massimo = numero
print(f"Il numero massimo della sequenza è: {massimo}")