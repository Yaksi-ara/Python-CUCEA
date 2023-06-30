import mysql.connector
selectrBaseDeDatos = 1
def conexion(selectorBasedeDatos):
    if selectorBasedeDatos == 'local':
        host="127.0.0.1"
        user="root" # root
        passwd="" # ""
        port = 3306
        database='mini-siiau'   
    elif selectorBasedeDatos == 'remoto':
        host="142.44.163.242"
        user="Alumno13"
        passwd="AlumnoPython1@."
        port = 4000
        database='mini-siiau'
    conexion = mysql.connector.connect(
        host = host,
        user = user,
        passwd = passwd,
        port = port,
        database = database);
    return conexion  #esta variable hace la conexión, por eso el try and catch; si esta función sirve, ps esto, y si no f