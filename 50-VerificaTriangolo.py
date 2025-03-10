lato1 = float(input("Inserire primo lato: "))
lato2 = float(input("Inserire secondo lato: "))
lato3 = float(input("Inserire terzo lato: "))
if lato1 == lato2 and lato1 == lato3 and lato2 == lato3:
    print("Il triangolo è equilatero")
elif lato1 == lato2 or lato1 == lato3 or lato2 == lato3:
    print("Il triangolo è iscoscele")
elif lato1 != lato2 or lato2 != lato3:
    print("Il triangolo è scaleno")
