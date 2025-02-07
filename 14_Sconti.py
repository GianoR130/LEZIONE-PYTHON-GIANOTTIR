jeans1 = int(input("Inserisci il prezzo del primo paio di jeans: "))
jeans2 = int(input("Inserisci il prezzo del secondo paio di jeans: "))
sconto = 0.20
totale = jeans1+jeans2
prezzo_scontato = totale * sconto
print("Il prezzo scontato è:",prezzo_scontato)
contanti = int(input("Inserisci i contanti: "))
resto = contanti-prezzo_scontato
print("Resto: ",resto)