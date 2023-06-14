mylist = [1,5,7,11,6,3,9] #así se define una lista 
print(mylist)
print(mylist[2]) #para imprimir un elemento específico, empezando de 0, en este caso, quiero el 11, entonces es 2
print(len(mylist)) #lenght, numero d elementos
mylist.append(13) #añadir o apilar elementos a la lista al final, en ese caso, el 13
mylist.remove(13) #elimina un elemento
print(mylist)
milista = mylist.copy #copia una lista
mylist.sort()

for count, element in enumerate(mylist):
    print(f"contador{count} - element {element}")
if 7 in mylist:
    print("Sí está el 7")
    print("posisión ordenada de 0 a 6, en",mylist.index(7))  
    #verifiq si una palabra es palíndromo, si una palabra es pangram, calcular el promedio
    # de una clase de 10 alumnos usando funciones y listas, verificar si una palabra se encuentra en otra, al derecho y al revés e imprima un si si se encuentra contenida, y un no si no se encuentra contenida
    
    