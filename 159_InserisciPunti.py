stringa = input("Inserira una stringa: ")
punto = 0
stringa_finale=""
for i in stringa:
    stringa_finale=stringa_finale+"." * punto + i
    punto += 1
print(stringa_finale)   