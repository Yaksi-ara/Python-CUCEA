frase= (input("Escribe una frase: "))
vocal= ("a","e","i","o","u")
for letter in frase:
    if letter.lower() in vocal:
        print(letter)


