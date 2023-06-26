import mysql.connector
opcionDB = 1

if opcionDB == 1 : 
#Local
 host = "127.0.0.1"
 user= "root"
 password = ""
 port = "3306"
 database = "mini-siiau"

elif opcionDB == 2: 
#REMOTA
 host = "142.44.163.242"
 user= "Alumno13"
 password = "AlumnoPython1@."
 port = "4000"
 database = "mini-siiau"

try: 
    conexion = mysql.connector.connect(
    host= host, 
    user= user, 
    password= password,
    database = database
    )
    print("Se estableció la conexión")
except mysql.connector.Error as err:
 print("Ocurrió un error al establecer conexión: ", err)

finally:
 conexion.close()