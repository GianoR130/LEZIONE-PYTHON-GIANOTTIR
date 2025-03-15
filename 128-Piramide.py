asterisco = 0
for r in range (1,11):
    print("*_" * asterisco)
    asterisco += 1
for j in range (1,12):
    if asterisco > 0:
        print("*_" * asterisco)
        asterisco -= 1
