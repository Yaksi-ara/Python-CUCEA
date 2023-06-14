#PALINDROMO

palabra = input("Ingresa una palabra: ")

def palindromo (palabra):
    palabra = palabra.lower()
    letras = list(palabra)
    
    invertida = list(reversed(letras))

    if letras == invertida:
        return True
    else:
        return False

if palindromo (palabra):
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")