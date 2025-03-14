n = int(input("Inserire un numero: "))
for r in range(0,n+1):
    for j in range(0,n+1):
        if r + j == n:
            print(r,",",j)