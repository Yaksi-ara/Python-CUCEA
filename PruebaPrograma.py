from Funciones import clear
import time
def compra():
 Precio =(int(input("Ingresa precio: "))) 
 Cantidad = (int(input("Ingresa cantidad que quieres comprar: ")))
 Nombre = (input("Ingresa tu nombre: "))
 CostoT = (Precio * Cantidad)
 Descuento = 0

 if Cantidad == 18 or Nombre.lower() == "Yaksi" : 
    print("Tienes un descuento especial del 20%")
    print("Total a pagar: ", (CostoT - Descuento), "pesos")
    
 elif Cantidad > 10:
    Descuento = (Precio * Cantidad)*.10 
    print("Tienes un descuento del 10%")
    print("Total a pagar: ", (CostoT - Descuento), "pesos")
    
 else: 
    print ("El costo es de: ", CostoT , "pesos")

def Notadeventa():
 print ("Nota de venta" .center(60,"-"))
 print("Las manzanas están en: " + str(Precio) , "pesos") 
 print("Compraste: " ,Cantidad, "manzanas" )

def bye():
 if (Descuento > 0): 
    print("El descuento fue de: ", Descuento, "pesos")
 while CantidadManzanas == 0:
        print("No se vendió ninguna manzana, ta bien")
        break

time.sleep(3)
clear()
print("Listo")