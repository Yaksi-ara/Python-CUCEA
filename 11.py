import pymysql #importamos el módulo
try: 
    '''los try-catch son una función que ejecuta un bloque, y si todo funciona hace algo, 
pero si no te dice el error, pero no rompe el programa'''
    conexion = pymysql.connect(host= 'localhost', 
                               user= 'root', 
                               password='',
                               db='peliculas')
    print("Se estableció la conexión")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
    print("Ocurrió un error al establecer conexión: ", e)