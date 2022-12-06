#Clases Admin y Cliente

from baseDeDatos import Conexion_BD

class Admin:
    def __init__(self, usuario, password, correo, id, nombre, apellido, cargo, tipoDeUsuario ='Admin'):
        self.__usuario = usuario
        self.__password = password
        self.__correo = correo
        self.__id = id
        self.__nombre = nombre
        self.__apellido = apellido
        self.__cargo = cargo
        self.__tipoDeUsuario = tipoDeUsuario
    

    # Getters
    @property
    def usuario(self):
        return self.__usuario
    @property
    def password(self):
        return self.__password
    @property
    def correo(self):
        return self.__correo
    @property
    def id(self):
        return self.__id
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def cargo(self):
        return self.__cargo
    @property
    def tipoDeUsuario(self):
        return self.__tipoDeUsuario


    # Setters
    @usuario.setter
    def usuario(self,nuevoUsuario):
        self.__usuario = nuevoUsuario
    @password.setter
    def password(self,nuevaPassword):
        self.__password = nuevaPassword
    @correo.setter
    def correo(self,nuevoCorreo):
        self.__correo = nuevoCorreo
    @id.setter
    def id(self,nuevoId):
        self.__id = nuevoId
    @tipoDeUsuario.setter
    def tipoDeUsuario(self,nuevoTipoDeUsuario):
        self.__tipoDeUsuario = nuevoTipoDeUsuario
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    @apellido.setter
    def apellido(self, nuevoApellido):
        self.__apellido = nuevoApellido
    @cargo.setter
    def cargo(self, nuevoCargo):
        self.__cargo = nuevoCargo

    def verReservaParticular():
        pass
    def crearSala(self, totalButacas, es3D):
        conexion=Conexion_BD("BaseDeDatos.db")
        conexion.insertar(f"INSERT INTO Sala (totalButacas, es3D) values (?,?)", (totalButacas, es3D))
       
    def modificarSala():
        pass
    def eliminarSala(self,id_Sala):
        conexion=Conexion_BD("BaseDeDatos.db")
        conexion.consulta(f"DELETE FROM Sala WHERE id = {id_Sala}")
        conexion.commit()
        conexion.cerrar()
    def modificarDescuentos():
        pass
    def crearFuncion():
        pass
    def modificarFuncion():
        pass
    def eliminarFuncion():
        pass
    def quitarPelicula(self, idPelicula):
        conexion = Conexion_BD("BaseDeDatos.db")
        conexion.consulta(f"DELETE FROM Peliculas WHERE id = {idPelicula}")
        conexion.commit()
        conexion.cerrar()



class Cliente:
    def __init__(self, usuario, password, correo, nombre, apellido, fechaNacimiento, id, tarjetaDeDescuento, tipoDeUsuario = 'Cliente'):
        self.__usuario = usuario
        self.__password = password
        self.__correo = correo
        self.__nombre = nombre
        self.__apellido = apellido
        self.__fechaNacimiento = fechaNacimiento
        self.__id = id
        self.__tarjetaDeDescuento = tarjetaDeDescuento
        self.__tipoDeUsuario = tipoDeUsuario
        
    
    @property
    def usuario(self):
        return self.__usuario
    @property
    def password(self):
        return self.__password
    @property
    def correo(self):
        return self.__correo
    @property
    def id(self):
        return self.__id
    @property
    def tipoDeUsuario(self):
        return self.__tipoDeUsuario
    @property
    def nombre(self):
        return self.__nombre
    @property
    def apellido(self):
        return self.__apellido
    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento
    @property
    def tarjetaDeDescuento(self):
        return self.__tarjetaDeDescuento

    # Esta sería tarea del Admin?
    @usuario.setter
    def usuario(self,nuevoUsuario):
        self.__usuario = nuevoUsuario
    @password.setter
    def password(self,nuevaPassword):
        self.__password = nuevaPassword
    @correo.setter
    def correo(self,nuevoCorreo):
        self.__correo = nuevoCorreo
    @id.setter
    def id(self,nuevoId):
        self.__id = nuevoId
    @tipoDeUsuario.setter
    def tipoDeUsuario(self,nuevoTipoDeUsuario):
        self.__tipoDeUsuario = nuevoTipoDeUsuario
    @nombre.setter
    def nombre(self, nuevoNombre):
        self.__nombre = nuevoNombre
    @apellido.setter
    def apellido(self, nuevoApellido):
        self.__apellido = nuevoApellido
    @fechaNacimiento.setter
    def fechaNacimiento(self, nuevaFechaNacimiento):
        self.__fechaNacimiento = nuevaFechaNacimiento
    @tarjetaDeDescuento.setter
    def tarjetaDeDescuento(self, nuevaTarjeta):
        self.__tarjetaDeDescuento = nuevaTarjeta

    def registrarse(self):
        conexion=Conexion_BD("BaseDeDatos.db")
        if conexion.consulta(f"SELECT correo FROM Clientes WHERE correo = '{self.correo}'")!=None:
            conexion.insertar("insert into Clientes (usuario, password, correo, nombre, apellido, fechaNacimiento, tarjetaDeDescuento, tipoDeUsuario) values (?,?,?,?,?,?,?,?)",(self.usuario, self.password, self.correo, self.nombre, self.apellido, self.fechaNacimiento,self.tarjetaDeDescuento, self.tipoDeUsuario))
        
    def login(self, usuario, password):
        conexion=Conexion_BD("BaseDeDatos.db")
        if conexion.consulta(f"SELECT * FROM Clientes WHERE usuario = '{usuario}' AND '{password}' == password"):
                print('Logged in')

        else:
            print('Revise los datos ingresados')
        conexion.cerrar()

    #def reservar(self):
        #conexion=Conexion_BD('BaseDeDatos.db')
        #conexion.insertar("INSERT INTO Reservas (id_Funcion, id_Cliente) VALUES (?,?)", (self.id_Funcion, self.id))

    def modificarReserva():
        pass
    def verReservas():
        conexion=Conexion_BD('BaseDeDatos.db')
        conexion.consulta(f"SELECT * FROM Reservas WHERE id = {id}")
        mostrarreservas=conexion.consulta
        print(mostrarreservas)
    def historialReservas():
        pass

#con=Conexion_BD("BaseDeDatos.db")
#con.consulta("INSERT INTO Clientes VALUES ('lisandrocinemark','licmark','lisandrogarcia@gmail.com','Lisandro', 'García','12/10/80','Jefe de ventas','No','Admin')")
#con.consulta("CREATE TABLE Clientes (usuario Text Primary Key, password Text, correo Text, nombre Text, apellido Text, fechaNacimiento Text, id Integer auto increment, tarjetaDeDescuento Text, tipoDeUsuario Text)")
#con.consulta("CREATE TABLE Administradores (usuario Text Primary Key, password Text, correo Text, id Integer auto increment, nombre Text, apellido Text, cargo Text, tipoDeUsuario Text)")
#con.consulta("CREATE TABLE Peliculas (id Integer Primary Key autoincrement, Titulo Text, Estreno Text, Genero Text, Duracion Integer, Director Text, Descripcion Text, Clasificacion Text)")
#con.consulta("CREATE TABLE Reservas (id Integer Primary Key autoincrement, id_Funcion Integer, id_Cliente Text, Foreign Key(id_Funcion) REFERENCES Funciones(id), Foreign Key(id_Cliente) REFERENCES Clientes(usuario))")
#con.consulta("CREATE TABLE Salas (id Integer Primary Key, totalButacas Integer, es3D Text)")
#con.consulta("CREATE TABLE Funciones (id Integer Primary Key autoincrement, Fecha Text, Hora Text, totalButacas Integer, id_Sala Integer, id_Pelicula Integer, Foreign Key(id_Sala) REFERENCES Salas(id), Foreign Key(id_Pelicula) REFERENCES Peliculas(id))")
#con.consulta("CREATE TABLE Detalle_Reservas (id Integer Primary Key autoincrement, id_Reserva Integer, butacasReservadas Integer, Foreign Key(id_Reserva) REFERENCES Reservas(id))")
#con.commit()
#con.cerrar()