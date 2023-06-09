PrecioManzanas =(int(input("Ingresa precio manzanas: "))) 
CantidadManzanas = (int(input("Ingresa cantidad manzanas que quieres comprar: ")))
Nombre = (input("Ingresa tu nombre: "))
CostoT = (PrecioManzanas * CantidadManzanas)
Descuento = 0
if CantidadManzanas == 18 or Nombre.lower() == "Yaksi" : 
    Descuento = (PrecioManzanas * CantidadManzanas)*.20
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
else :
    print ("No hubo descuento")

 #cuando se compren 0 manzanas, tiene q decirte a, tabien
