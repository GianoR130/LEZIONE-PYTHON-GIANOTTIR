studenti = ["Arianna","Bruno","Dario","Elena","Mario","Teresa"]
studente_cercato=input("Scrivi il nome dello studente: ")
if studente_cercato in studenti:
   print(studente_cercato, "è uno studente di questa scuola")
elif studente_cercato not in studenti:
   print(studente_cercato,"non è un nostro studente")