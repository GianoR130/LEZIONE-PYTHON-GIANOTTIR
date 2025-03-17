input = input("Scegliere il codice c1 o c2: ")
c1 = "AFCDDR-CF-2020"
c2 = "SEDTYR-XC-2019"
if input == "c1":
    if c1.endswith("2020"):
        print("Il codice c1 termina con 2020:",c1)
elif input == "c2":
    if c2.endswith("2019"):
        print("Il codice c2 termina con 2019:",c2)