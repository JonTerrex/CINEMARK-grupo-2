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

    def login():
        pass
    def verReservaParticular():
        pass
    def crearSala():
        pass
    def modificarSala():
        pass
    def eliminarSala():
        pass
    def modificarDescuentos():
        pass
    def crearFuncion():
        pass
    def modificarFuncion():
        pass
    def eliminarFuncion():
        pass



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
        if conexion.consulta(f"select correo from Clientes where correo='{self.correo}'")!=None:
            conexion.insertar("insert into Clientes (usuario, password, correo, nombre, apellido, fechaNacimiento, tarjeta, tipoDeUsuario) values (?,?,?,?,?,?,?,?)",(self.usuario, self.password, self.correo, self.nombre, self.apellido, self.tarjetaDeDescuento, self.tipoDeUsuario))
    
    def login():
        pass
    def reservar():
        pass
    def moficarReserva():
        pass
    def verReservas():
        pass
    def historialReservas():
        pass

con=Conexion_BD("BaseDeDatos.db")
#con.consulta("CREATE TABLE Clientes (usuario Text Primary Key, password Text, correo Text, nombre Text, apellido Text, fechaNacimiento Text, id Integer auto increment, tarjetaDeDescuento Text, tipoDeUsuario Text)")
#con.consulta("CREATE TABLE Administradores (usuario Text Primary Key, password Text, correo Text, id Integer auto increment, nombre Text, apellido Text, cargo Text, tipoDeUsuario Text)")
con.commit()
con.cerrar()
