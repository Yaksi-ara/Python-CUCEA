import pymysql #importamos el módulo
try: 
    '''los try-catch son una función que ejecuta un bloque, y si todo funciona hace algo, 
pero si no te dice el error, pero no rompe el programa'''
    conexion = pymysql.connect(host= 'localhost', 
                               user= 'root', 
                               password='',
                               db='peliculas')
    print("Se estableció la conexión")
except mysql.connector.Error as err:
    print("Ocurrió un error al establecer conexión: ", err)
    
import mysql.connector
db = mysql.connector.connect(
    host= "127.0.0.1"
    user= "root"
    password= "password") finally:
db.close()