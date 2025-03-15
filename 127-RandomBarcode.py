import random
for i in range (40):
    lancio = random.randint(0,1)   
    if lancio == 0:
        print("|",end="")
    elif lancio == 1:
        print(" ",end="")