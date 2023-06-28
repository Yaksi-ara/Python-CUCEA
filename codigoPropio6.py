#PARA AÑADIR UN ELEMENTO A materia

import funcionDeConexion 
import mysql.connector
def interfazSql(id,title):
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

# CTRL + TECLA DE ] GENERA UN #