#PARA HACER UN DELETE

import funcionDeConexion 
import mysql.connector
def interfazSql(id,title):
    try: 
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        sql = f"DELETE FROM materia WHERE title = '{title}' AND id = '{id}'";
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
        
interfazSql('1001','Administracion')