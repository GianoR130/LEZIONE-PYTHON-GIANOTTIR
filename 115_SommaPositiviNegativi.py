p = int(input("Inserire numero positivo: ")) 
n = int(input("Inserire numero negativo: "))
if n < 0:
    n = -n

somma_positiva = 0 
somma_negativa = 0

for i in range(1, p+1):
    somma_positiva += i

for i in range(-1, -n-1, -1):
    somma_negativa += i

print("Somma numeri positivi:", somma_positiva)
print("Somma numeri negativi:", somma_negativa)