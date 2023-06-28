#PARA HACER UPDATE EN materia

import funcionDeConexion 
import mysql.connector
def interfazSql(id,title):
    try: 
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        sql = f"UPDATE materia SET id = {id} where title = '{title}';" #NO USAR ' O ", USAR COMILLA FRANCESA O NO USAR
        print(sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("Failed to update because record to database rollback: {}".format(error)) #reverting changes because of exception
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()
interfazSql('1001','Administracion')