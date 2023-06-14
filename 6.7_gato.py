#"verifique si una palabra se encuentra contenida en otra, al derecho y al reves e imprima un si, si se encuentra contenida, y un no si no se encuentra contenida"
palabra1 = input("Ingresa una palabra: ")
palabra2 = input("Ingresa otra palabra: ")

def gato (palabra1, palabra2):
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    
    if palabra1 in palabra2 or palabra1 in palabra2[::-1]:
      return True
    return False

if gato (palabra1, palabra2):
    print("Sí")
else:
    print("No")


