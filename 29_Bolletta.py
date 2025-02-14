consumo = float(input("Inserisci il consumo in metri cubi: "))
quota_fissa = 20.0
if consumo < 500:
    primo_consumo = consumo * 0.575
    secondo_consumo = 0
else:
    primo_consumo = 500 * 0.575
    secondo_consumo = (consumo - 500) * 0.783
totale = quota_fissa + primo_consumo + secondo_consumo
print("Il totale è: ",totale)