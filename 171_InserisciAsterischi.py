q = 0
numero = input("Inserisci un asterisco: ")
while numero != "!":
    if numero != "*":
        print("Errore! Il carattere non è un asterisco!")
        break
    if numero == "*":
        if q < 9:
            q += 1 
            numero = input("Sono stati inseriti "+str(q)+" caratteri, inserire un asterisco (! per terminare): ")
        elif q == 9:
            q != 1
            break
print("Sono stati inseriti",q,"asterischi in totale")
