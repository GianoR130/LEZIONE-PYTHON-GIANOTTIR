l1 = float(input("Inserire il primo lato: "))
l2 = float(input("Insrire il secondo lato: "))
l3 = float (input("Inserire il terzo lato: "))
if l1 < (l2 + l3) or l2 < (l1 + l3) or l3 < (l1 + l2):
    print("La figura è un tirangolo")
else:
    print("La figura non è un triangolo")