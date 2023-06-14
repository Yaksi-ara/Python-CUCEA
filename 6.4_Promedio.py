#ejercicio calcular el promedio de una clase de 10 alumnos usando funciones y listas 

calificaciones = []
for x in range (10):
    nota = int(input("Ingresa calificación: "))
    calificaciones.append(nota)
    calificaciones.sort()
    
print("LISTA DE CALIFICACIONES".center(30,"-"))

for count, element in enumerate(calificaciones):
 print(f"Alumno {count} - calificación de {element}")

def promedio():
    total = sum(calificaciones)/10
    print("El promedio es de: ", total)
    return total

promedio()
print("Listo")

