#MI MENU BONITO <3

import Menu #nos trajimos nuestro menú 
import MateriaDAO

Menu.menuPrincipal() #podríamos hacer esto desde el import, pero mejor así por si luego nuestro Menu crece en funciones

opcion = input("Ingresa una opción: ")
if opcion == '1' :
    id = input('Ingresa el id: ')
    title = input('Ingresa el nombre de la materia: ')
    MateriaDAO.altaMateria(id,title)
elif opcion == '2' :
    id = input('Ingresa el id: ')
    MateriaDAO.verMateria(id)
elif opcion == '3' :
    MateriaDAO.verTodasMaterias()
elif opcion == '4' :
    id = input('Ingresa el id: ')
    title = input('Ingresa el nombre de la materia: ')
    MateriaDAO.modificarMateria(id,title)
elif opcion == '5' :
    title = input('Ingresa el nombre de la materia: ')
    MateriaDAO.borrarMateria(title)