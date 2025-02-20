import time
password = input("Inserire la password: ")
if password == "PincoPallino2022!":
    print("Password corretta!")
elif password != "PincPallino2022!":
    print("Password errata! Hai 3 tentativi rimasti!")
    time.sleep(1)
    password = input("Inserire la passowrd: ")
    if password == "PincoPallino2022!":
        print("Password corretta!")
    elif password != "PincoPallino2022!":
        print("Password errata! Hai 2 tentativi rimasti!")
        time.sleep(1)
        password = input("Inserire la password: ")
        if password == "PincoPallino2022!":
            print("Password corretta!")
        elif password != "PincoPallino2022!":
            print("Password errata! Hai 1 tentativo rimasto!")
            time.sleep(1)
            password = input("Inserire la password: ")
            if password == "PincoPallino2022!":
                print("Password corretta!")
            elif password != "PincoPallino2022!":
                print("Password errata! Hai 0 tentativi rimasti!")

""" password = "PincoPallino2022!"
tentativi = 3
risposta = input("Inserire la password: ")
while risposta != password and tentativi != 0:
    tentativi -= 1
    print("Password errata! Tentativi rimasti:",tentativi)
    if tentativi == 0:
        print("Hai terminato i tentativi.")
        break
    time.sleep(1)
    risposta = input("Inserire la password: ")
    if risposta == password:
        print("Password CORRETTA!")
        break """