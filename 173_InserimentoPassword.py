import time
pw1 = "Password66"
conferma = pw1
tentativi = 3
while True:
    ins = input("Inserire la password: ")
    if ins == pw1:
        print()
        time.sleep(1)
        print("Password corretta, accesso in corso.")
        break
    elif tentativi == 1:
        print("Errore: la password è errata, hai",tentativi,"tentativo rimasto.")
        tentativi -= 1
        print()
    elif tentativi == 0:
        print("Errore, la password è errata, hai",tentativi,"tenativi rimasti.")
        print("Riprova più tardi.")
        break
    elif ins != pw1:
        print("Errore: la password è errata, hai",tentativi,"tentativi rimasti.")
        tentativi -= 1
        print()