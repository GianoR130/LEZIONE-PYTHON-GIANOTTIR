import time
anno = int(input("Inserire l'anno di nascita: "))
print("La tua generazione è...")
time.sleep(1.5)
if anno < 1946:
    print("Prima dei boomer.")
elif anno > 1946 and anno < 1964:
    print("Boomer.")
elif anno > 1965 and anno < 1980:
    print("Generazione X.")
elif anno > 1981 and anno < 2000:
    print("Generazione Y.")
elif anno > 2000:
    print("Generazione Z")