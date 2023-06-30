#CRUD = CREATE, READ, UPDATE, DELETE
import ConectorBaseDeDatos
import mysql.connector
import Materia
 #esto es para no poner código en una función de mientras XD, existe pero a futuro sabrá q hacer >pass<
 
 
def altaMateria(id, title):
    #poner código d insert
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        sql = f"INSERT INTO Materia (id, title) VALUES ('{id}', '{title}');"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()   
        
        

def verMateria(id):
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM materia where id = {id}') #SENTENCIA A EJECUTAR CONSOLA DE BD
        registros = cursor.fetchall() #FETCHALL agarra 
        for registro in registros:
            #materia = Materia(registro[0], registro[1]) #Registros 1 y 2
            print(f'id = {registro[0]} título = {registro[1]}') #imprime q mi materia es algo
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        cursor.close()
        conexion.close() #SI DA ERROR, ELIMINAR FINALLY Y CERRAR AMBOS EN EXCEPT Y TRY
        
        

def verTodasMaterias():
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM materia')
        registros = cursor.fetchall()
        for registro in registros:
            #materia = Materia(registro[0],registro[1])
            print(f'id = {registro[0]} titulo = {registro[1]}')
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close() 
        


def modificarMateria(id, title):
 try: 
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        sql = f"UPDATE materia SET id = {id} where title = '{title}';" 
        print(sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
 except mysql.connector.Error as error:
        print("Failed to update because record to database rollback: {}".format(error)) 
        cursor.close()
        conexion.close()

def borrarMateria(id):
    try: 
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        sql = f"DELETE FROM materia WHERE id = '{id}'";
        print(sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("Failed to update because record to database rollback: {}".format(error))
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()
