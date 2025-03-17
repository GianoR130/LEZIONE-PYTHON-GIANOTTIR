stringa = "Marco ieri è andato in piscina mentre Marco domani andrà in montagna."
input = input("Scrivere un nome: ")

if input == "Gianluca" or input == "Nicola" or input == "Mattia" or input == "Enea" or input == "Elia" or input == "Luca" or input == "Noa":
    nuova_stringa = stringa.replace("Marco",input)

elif input == "Andrea":
    nuova_stringa = stringa.replace("andato","andat@").replace("Marco", input)

elif input == "Samuele" or input == "Gabriele" or input == "Emanuele" or input == "Michele" or input == "Daniele" or input == "Dante":
    nuova_stringa = stringa.replace("Marco", input)

elif input.endswith("a") or input.endswith("e"):
    nuova_stringa = stringa.replace("andato","andata").replace("Marco", input)

elif input == "Iris":
    nuova_stringa = stringa.replace("andato","andata").replace("Marco", input)

else:
    nuova_stringa = stringa.replace("Marco",input)

print(nuova_stringa)