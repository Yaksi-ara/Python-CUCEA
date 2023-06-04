PrecioManzanas =(int(input("Ingresa precio manzanas: "))) # Se tiene que definir q tipo de variable se va a ingresar
CantidadManzanas = (int(input("Ingresa cantidad manzanas: "))) # en este caso int, pq si no podrías poner una letra x letra y eso q
print("El costo es de: ", PrecioManzanas * CantidadManzanas)

#PARA CONCATENAR para sumar cadenas de texto, forma 1:
print("Las manzanas están en: " + str(PrecioManzanas)) #SUMAMOS LETRAS
#FORMA 2
print("Fueron: " , CantidadManzanas , "manzanas" )
#FORMA 3
print(f"Total a pagar: {PrecioManzanas * CantidadManzanas}" )
