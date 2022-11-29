#Clases Usuario, Admin y Cliente
from Conexion.baseDeDatos import Conexion_BD

class Usuario:
    def __init__(self, usuario, password, correo, id, tipoDeUsuario):
        self.__usuario = usuario
        self.__password = password
        self.__correo = correo
        self.__id = id
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


    def __str__(self):
        datos = 'Usuario: '+ self.__usuario
        datos += '\nPassword: '+ str(self.__password)
        datos += '\nCorreo: '+ str(self.__correo)
        datos += '\nId: '+ str(self.__id)
        datos += '\nTipo de usuario: '+ self.__tipoDeUsuario
        return datos

    # Metodos
    def registrarse():
        pass

    def login():
        pass
    def insertar(self):
        c = Conexion_BD('BaseDeDatos.db')
        c.consulta(f"INSERT INTO Usuarios values ({self.usuario}',' {self.password}','{self.correo}','{self.id}','{self.tipoDeUsuario})")
        c.commit()
        c.cerrar()




class Admin(Usuario):
    def __init__(usuario, password, correo, id):
        super().__init__(usuario, password, correo, id, tipoDeUsuario = 'Admin')

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



class Cliente(Usuario):
    def __init__(self, usuario, password, correo, id, tarjetaDeDescuento):
        self.__tarjetaDeDescuento = tarjetaDeDescuento
        super().__init__(usuario, password, correo, id, tipoDeUsuario = 'Cliente')
        
    @property
    def tarjetaDeDescuento(self):
        return self.__tarjetaDeDescuento

    def reservar():
        pass
    def modificarReserva():
        pass
    def verReservas():
        pass
    def historialReservas():
        pass