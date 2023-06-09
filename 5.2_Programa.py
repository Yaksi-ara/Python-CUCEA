#TABLA DE MULTIPLICAR
#depurar/debug significa leer programa líneaxlínea
#debug sirve aquí, para saber en qué ciclo iría, por ejemplo, cuando el contador valga 4
contador = 0
numero = (int(input("¿Qué número quieres multiplicar? " )))
while contador <= 100 : 
    print(f"{numero} * {contador} = {numero * contador}")
    contador = contador + 1
    contador+=1