n = int(input("Inserire un numero: "))
asterisco = 1
for i in range(1,n+1):
    if i % 2 == 0:
        print("*")
    else:
        print("*" * asterisco)
        asterisco += 1
