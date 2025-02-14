velocita = int(input("Il limite di velocità è di 80 km/h, inserire la velocità del veicolo: "))
if velocita <= 80:
    print("La velocità del veicolo non ha superato il limite di velocità.")
elif velocita > 80 and velocita <= 90:
    print("La sanzione sarà di 36 euro.")
elif velocita > 90 and velocita <= 120:
    print("La sanzione sarà di 148 euro.")
elif velocita > 120 and velocita <= 140:
    print("La sanzione sarà di 370 euro.")
elif velocita > 140:
    print("La sanzione sarà di 500 euro.")