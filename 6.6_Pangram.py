#PANGRAM

palabra = input("Ingresa una palabra o frase: ")
palabra = palabra.strip()

def pangram (palabra):
    palabra = palabra.lower()
    alfabeto = ["q" ,"w" ,"e" ,"r" ,"t" ,"y" ,"u" ,"i" ,"o" ,"p" ,"a" ,"s" ,"d" ,"f" ,"g" ,"h" ,"j" ,"k" ,"l" ,"z" ,"x" ,"c" ,"v" ,"b" ,"n" ,"m"]
    
    for letter in alfabeto:
      if letter not in palabra:
         return False
     
    return True

if pangram (palabra):
    print("La palabra es un pangram")
else:
    print("La palabra no es pangram")