n = int(input("Inserire un numero: "))
if n == 2:
    print("Il numero inserito è un numero primo")
elif n % 2 == 0:
    print("Il numero inserito non è un numero primo")
elif n % 3 == 0:
    print("Il numero inserito non è un numero primo")
elif n % 5 == 0:
    print("Il numero inserito non è un numero primo")
else:
    print("Il numero inserito è un numero primo")