import sqlite3 as sql

class Conexion_BD():

    def __init__(self,bd):
        self.conexion = sql.connect(bd)
        self.cursor = self.conexion.cursor()

    def consulta(self, consulta):
        self.cursor.execute(consulta)
    
    def commit(self):
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()

cbd = Conexion_BD('BaseDeDatos.db')
cbd.consulta("CREATE TABLE IF NOT EXISTS Usuarios (usuario Text, password Text, correo Text, id INTEGER PRIMARY KEY AUTOINCREMENT, tipoDeUsuario Text)")
cbd.consulta("CREATE TABLE IF NOT EXISTS Sala (id Integer primary key, totalButacas Integer, es3D Integer)")
cbd.consulta("""CREATE TABLE IF NOT EXISTS Funcion 
(id Integer primary key, 
fecha Date, 
hora Text, 
butacasLibres Integer,
es3D Integer, 
id_Sala Integer, 
foreign key(id_Sala) references Sala(id)), 
id_Pelicula Integer, 
foreign key(id_Pelicula) references Pelicula(id)""")

cbd.consulta("CREATE TABLE IF NOT EXISTS Pelicula (id Integer primary key, titulo Text, fechaEstreno Text, genero Text, duracion Integer, director Text, descripcion Text, clasificacion Text")
cbd.consulta("CREATE TABLE IF NOT EXISTS Reservas (id Integer primary key autoincrement, id_Usuario Integer, foreign key (id_Usuario) references Usuarios(id), id_Funcion Integer, foreign key(id_Funcion) references Funcion(id))")

cbd.consulta("""insert into Usuarios (usuario, password, correo, tipoDeUsuario) values 
('josearaujo','ewroihf7hfuw','jaraujo@gmail.com','Admin'),
('pabloarcodaci','sdfafiuh45jf','parcodaci@outlook.com','Cliente'),
('nicoasdu','f34hu5f','nicoa@yahoo.com','Admin')""")

cbd.consulta("insert into Sala values (1, 150, 0), (2, 140, 1), (3,160, 0)")
cbd.consulta("insert into Funcion values ()")
cbd.commit()
cbd.cerrar()
