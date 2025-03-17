stringa = input("Inserire una stringa: ")
for i in "aeiouAEIOU":
    stringa = stringa.replace(i, "*")
print("Stringa modificata:",stringa)