voto = float(input("inserire il voto: "))
if voto < 6:
   print("il voto è insufficiente")
elif voto == 6:
   print("il voto è sufficiente")
elif voto > 6 and voto < 9:
    print("Il voto va bene")
elif voto >= 9 and voto <= 10:
   print("Il voto è molto buono")