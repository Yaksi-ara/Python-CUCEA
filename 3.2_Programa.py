PrecioManzanas =(int(input("Ingresa precio manzanas: "))) 
CantidadManzanas = (int(input("Ingresa cantidad manzanas que quieres comprar: ")))
Descuento = (PrecioManzanas * CantidadManzanas)*.10 
if CantidadManzanas >= 10:
    print("Tienes un descuento del 10%, tienes que pagar: ", (PrecioManzanas * CantidadManzanas - Descuento), "pesos")
else: 
    print("El costo es de: ", PrecioManzanas * CantidadManzanas)
print("Las manzanas están en: " + str(PrecioManzanas))
print("Fueron: " , CantidadManzanas , "manzanas" )
