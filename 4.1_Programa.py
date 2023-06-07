PrecioManzanas =(int(input("Ingresa precio manzanas: "))) 
CantidadManzanas = (int(input("Ingresa cantidad manzanas que quieres comprar: ")))
Nombre = (input("Ingresa tu nombre: "))
CostoT = (PrecioManzanas * CantidadManzanas)

if CantidadManzanas == 18 or Nombre.lower() == "Yaksi" : #Ese importa más q la otra condición jerárquicamente, si fuera al revés, el programa marcaría q no hay descuento secreto
    Descuento = (PrecioManzanas * CantidadManzanas)*.20
    print("Tienes un descuento especial del 20%, tienes que pagar: ", (CostoT - Descuento), "pesos")
elif CantidadManzanas > 10:
    Descuento = (PrecioManzanas * CantidadManzanas)*.10 
    print("Tienes un descuento del 10%, tienes que pagar: ", (CostoT - Descuento), "pesos")
else: 
    print ("El costo es de: ", CostoT , "pesos")
print ("Nota de venta" .center(60,"-"))
print("Las manzanas están en: " + str(PrecioManzanas) , "pesos") 
print("Compraste: " , CantidadManzanas , "manzanas" )
if (Descuento > 0): 
    print("El descuento fue de: ", Descuento, "pesos")
else :
    print ("No hubo descuento")
 #pesos a dolares, a euros, yanes, dolares a euros, dolares a yuanes y euros a yuanes