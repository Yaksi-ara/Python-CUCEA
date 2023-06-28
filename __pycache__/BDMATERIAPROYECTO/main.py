#MI MENU BONITO <3

import Menu #nos trajimos nuestro menú 
import MateriaDAO

Menu.menuPrincipal() #podríamos hacer esto desde el import, pero mejor así por si luego nuestro Menu crece en funciones

opcion = input("Ingresa una opción: ")
if opcion == 1:
    id = input("Inserta el id")
    title = input("Inserta el id")
     MateriaDAO.altaMateria(id, title)

if opcion == 2:
     MateriaDAO.verTodasMaterias()