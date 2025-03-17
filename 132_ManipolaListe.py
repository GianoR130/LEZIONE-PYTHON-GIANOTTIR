studenti = ["Arianna","Bruno","Dario","Elena","Mario","Teresa"]
studenti.append("Domenico")
studenti[3]="Gabriel"
studenti.remove("Bruno")
studenti.remove("Teresa")
for x in range(len(studenti )):
    print(x,studenti[x])