from Funciones import clear
import time

PrecioManzanas =(int(input("Ingresa precio manzanas: "))) 
CantidadManzanas = (int(input("Ingresa cantidad manzanas que quieres comprar: ")))
Nombre = (input("Ingresa tu nombre: "))
CostoT = (PrecioManzanas * CantidadManzanas)
Descuento = 0

if CantidadManzanas == 18 or Nombre.lower() == "Yaksi" : 
    print("Tienes un descuento especial del 20%")
    print("Total a pagar: ", (CostoT - Descuento), "pesos")
    
elif CantidadManzanas > 10:
    Descuento = (PrecioManzanas * CantidadManzanas)*.10 
    print("Tienes un descuento del 10%")
    print("Total a pagar: ", (CostoT - Descuento), "pesos")
    
else: 
    print ("El costo es de: ", CostoT , "pesos")
    
print ("Nota de venta" .center(60,"-"))
print("Las manzanas están en: " + str(PrecioManzanas) , "pesos") 
print("Compraste: " , CantidadManzanas , "manzanas" )

if (Descuento > 0): 
    print("El descuento fue de: ", Descuento, "pesos")
while CantidadManzanas == 0:
        print("No se vendió ninguna manzana, ta bien")
        break

time.sleep(3)
clear()
print("Listo")

#además ahora tienes q vender peras y duraznos, usa una función