numero = int(input("Inserisci un numero: "))
originale = numero
fattori_primi = []
for i in range(2, originale + 1):
    while numero % i == 0:
        fattori_primi.append(i)
        numero = numero // i
print("Fattori primi:", fattori_primi)