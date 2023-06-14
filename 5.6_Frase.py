
 #soliticar al usuario q ingrese una frase y luego imprimir un listado de las vocales que aparecen en 
 # esa frase sin repetirlas, IMPORTANTE EN ENTREVISTAS, usa for o if
comprobacionA = comprobacionE = comprobacionI = comprobacionO = comprobacionU = False
frase= (input("Escribe una frase: ".lower()))

for letter in frase:
    print(letter)
    if "a" in letter.lower() and comprobacionA == False:
        print("a")
        comprobacionA = True
    if "e" in letter.lower() and comprobacionE == False:
        print("e")
        comprobacionE = True
    if "i" in letter.lower() and comprobacionI == False:
        print("i")
        comprobacionI = True
    if "o" in letter.lower() and comprobacionO == False:
        print("o")
        comprobacionO = True
    if "u" in letter.lower() and comprobacionU == False:
        print("u")
        comprobacionU = True
    
    
#escribe un programa q pida 2 numeros enteros q escriba q nmeros son pares y cuales impartes desde el primero hasta el segundo
 # imprimir todos los números del 5 al 20 altando de 3 en 3
 # ctrl L limpia terminal
 
 