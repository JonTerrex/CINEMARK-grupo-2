import sqlite3 as sql

class Conexion_BD():

    def __init__(self,bd):
        self.conexion = sql.connect(bd)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
        self.cursor.execute(consulta)
        return self.cursor.fetchall()

    def insertar(self, consulta, value):
        self.cursor.execute(consulta, value)
        self.conexion.commit()
        ultimo_id = self.cursor.lastrowid
        self.conexion.close()
        return ultimo_id
 
    def actualizar(self, consulta, value):
        self.cursor.execute(consulta, value)
        self.conexion.commit()
        self.conexion.close()

    # try DELETE except id_error 
    def eliminar(self, consulta, value):
        self.cursor.execute(consulta, value)
        self.conexion.commit()
        self.conexion.close()
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()