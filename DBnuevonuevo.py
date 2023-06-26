import mysql.connector

opcionBaseDeDatos = 1

if opcionBaseDeDatos == 1:
    # Forma local
    host = "localhost"
    user = "root"
    passwd = ""
    port = 3306
elif opcionBaseDeDatos == 2:
    # Forma remota
    host = "142.44.163.242"
    user = "Alumno13"
    passwd = "AlumnoPython1@."
    port = 4000

conexion = None  # Define la variable conexion antes del bloque try
try:
    conexion = mysql.connector.connect(
        host=host,
        user=user,
        passwd=passwd,
        port=port
    )
    print("Se estableció conexión")
except mysql.connector.Error as err:
    print("Ocurrió un error al establecer conexión: ", err)
finally:
    if conexion is not None:
        conexion.close()
