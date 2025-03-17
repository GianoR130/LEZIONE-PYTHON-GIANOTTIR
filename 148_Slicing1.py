stringa = input("Scrivere una stringa: ")
if len(stringa) > 4:
    print(stringa[1:5])
elif len(stringa) <= 4:
    print("Caratteri insufficienti.")