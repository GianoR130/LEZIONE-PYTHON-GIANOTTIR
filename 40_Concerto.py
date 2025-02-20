risposta1 = input("Mi accompagni al concerto dei Maneskin? ")
if risposta1 == "Si":
    risposta2 = input("Va bene andare Sabato? ")
    if risposta2 == "Si":
        print("Molto bene, prenoto i biglietti per Sabato!")
    elif risposta2 == "No":
        print("Peccato, io sono libero solo il Sabato!")    
else:
    print("Allora chiederò a qualcun altro")
