#CRUD = CREATE, READ, UPDATE, DELETE
import ConectorBaseDeDatos
import mysql.connector
import Materia
 #esto es para no poner código en una función de mientras XD, existe pero a futuro sabrá q hacer pass
def altaMateria(id, title):
    #poner código d insert
 try: 
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        sql = f"INSERT INTO materia (`id`, `title`) VALUES ('{id}', '{title}');" #NO USAR ' O ", USAR COMILLA FRANCESA O NO USAR
        print(sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("Failed to update because record to database rollback: {}".format(error)) #reverting changes because of exception
        conexion.rollback()
interfazSql('5','Administracion')    

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
        conexion.close()

def verTodasMaterias():
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM materia') #SENTENCIA A EJECUTAR CONSOLA DE BD
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
        

def modificarMateria(id, title):
    pass

def borrarMateria(id):
    pass

def borrarMateria():
    pass
