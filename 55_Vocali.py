input = input("Inserire un carattere: ").lower()
if input in "aeiou":
    print("Il carattere è una vocale")
elif input in "bcdfghlmnpqrstvz":
    print("Il carattere è una consonante")
else:
    print("Il carattere non è ne una consonante ne una vocale")