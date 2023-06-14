#FUNCIÓN = MÓDULO
import os #import para agarrar la función/módulo de otro lado

def clear():
  if os.name == "ce" or os.name == "nt" or os.name == "dos":
   os.system = ("cls")
   
def saludo (): #def nombredelafuncion (): 
    print("Hola, buenas tardes")
    print("Tengo sueño ayuda")
clear()
saludo() #así se manda a llamar una función
print("Adiós")


#puede importar funciones de tus propios archivos, import nombredelarchivo y la llamas con nombredelarchivo.nombredelafunción()