#Clases: Funcion, Sala, Funciones, Pelicula, Catalogo
from baseDeDatos import Conexion_BD
class Funcion:
    def __init__(self, idFuncion, fecha, pelicula, butacasLibres, es3D, sala):
        self.__idFuncion = idFuncion
        self.__fecha = fecha
        self.__pelicula = pelicula
        self.__butacasLibres = butacasLibres
        self.__es3D = es3D
        self.__sala = sala
    
    # Getters
    @property
    def idFuncion(self):
        return self.__idFuncion
    @property
    def fecha(self):
        return self.__fecha
    @property
    def pelicula(self):
        return self.__pelicula
    @property
    def butacasLibres(self):
        return self.__butacasLibres
    @property
    def es3D(self):
        return self.__es3D
    @property
    def sala(self):
        return self.__sala


    # Setters
    @idFuncion.setter
    def idFuncion(self,nuevoIdFuncion):
        self.__idFuncion = nuevoIdFuncion
    @fecha.setter
    def fecha(self,nuevafecha):
        self.__fecha = nuevafecha
    @pelicula.setter
    def pelicula(self,nuevaPelicula):
        self.__pelicula = nuevaPelicula
    @butacasLibres.setter
    def butacasLibres(self,nuevasButacasLibres):
        self.__butacasLibres = nuevasButacasLibres
    @es3D.setter
    def es3D(self,nuevoEs3D):
        self.__es3D = nuevoEs3D
    @sala.setter
    def sala(self,nuevaSala):
        self.__sala = nuevaSala

    def __str__(self):
        datos = 'idFuncion: '+ str(self.__idFuncion)
        datos += '\nFecha: '+ str(self.__fecha)
        datos += '\nPelicula: '+ str(self.__pelicula)
        datos += '\nButacas Libres: '+ str(self.__butacasLibres)
        datos += '\nEs 3D: '+ str(self.__es3D)
        datos += '\nSala: '+ str(self.__sala)
        return datos



class Sala:
    def __init__(self, totalDeButacas, es3D, numeroDeSala):
        self.__totalDeButacas = totalDeButacas
        self.__es3D = es3D
        self.__numeroDeSala = numeroDeSala

    # Getters
    @property
    def totalDeButacas(self):
        return self.__totalDeButacas
    @property
    def es3D(self):
        return self.__es3D
    @property
    def numeroDeSala(self):
        return self.__numeroDeSala


    # Setters
    @totalDeButacas.setter
    def totalDeButacas(self,nuevoTotalDeButacas):
        self.__totalDeButacas = nuevoTotalDeButacas
    @es3D.setter
    def es3D(self,nuevoEs3D):
        self.__es3D = nuevoEs3D
    @numeroDeSala.setter
    def numeroDeSala(self,nuevoNumeroDeSala):
        self.__numeroDeSala = nuevoNumeroDeSala

    def __str__(self):
        datos = 'Total de Butacas: '+ str(self.__totalDeButacas)
        datos += '\n3D: '+ str(self.__es3D)
        datos += '\nNúmero de Sala: '+ str(self.__numeroDeSala)



class Funciones:
    def __init__(self, funciones=[]):
        self.__funciones = funciones
    
    @property
    def funciones(self):
        return self.__funciones
    @funciones.setter
    def funciones(self, nuevasFunciones):
        self.__funciones = nuevasFunciones
    
    def listarFunciones():
        pass
        



class Pelicula:
    def __init__(self, titulo, estreno, genero, duracion, director, descripcion, clasificacion):
        self.__id = id
        self.__titulo = titulo
        self.__estreno = estreno
        self.__genero = genero
        self.__duracion = duracion
        self.__director = director
        self.__descripcion = descripcion
        self.__clasificacion = clasificacion

    #Getters
    @property
    def id(self):
        return self.__id
    @property
    def titulo(self):
        return self.__titulo
    @property
    def estreno(self):
        return self.__estreno
    @property
    def genero(self):
        return self.__genero
    @property
    def duracion(self):
        return self.__duracion
    @property
    def director(self):
        return self.__director
    @property
    def descripcion(self):
        return self.__descripcion
    @property
    def clasificacion(self):
        return self.__clasificacion

    #Setters
    @id.setter
    def id(self, nuevoid):
        self.__id = nuevoid
    @titulo.setter
    def titulo(self, nuevoTitulo):
        self.__titulo = nuevoTitulo
    @estreno.setter
    def estreno(self, nuevoestreno):
        self.__estreno = nuevoestreno
    @genero.setter
    def genero(self, nuevoGenero):
        self.__titulo = nuevoGenero
    @duracion.setter
    def duracion(self, nuevaDuracion):
        self.__duracion = nuevaDuracion
    @director.setter
    def director(self, nuevodirector):
        self.__director = nuevodirector
    @descripcion.setter
    def descripcion(self, nuevaDescripcion):
        self.__descripcion = nuevaDescripcion
    @clasificacion.setter
    def clasificacion(self, nuevaClasificacion):
        self.__clasificacion = nuevaClasificacion    


    def __str__(self):
        datos = 'Título: '+ self.__titulo
        datos += '\nGénero: '+ self.__genero
        datos += '\nDuración: '+ str(self.__duracion)
        datos += '\nDescripción: '+ self.__descripcion
        datos += '\nClasificación: '+ self.__clasificacion
        return datos

    def agregarPelicula(self):
        conexion = Conexion_BD("BaseDeDatos.db")
        conexion.insertar(f"INSERT INTO Peliculas (titulo, estreno, genero, duracion, director, descripcion, clasificacion) values (?,?,?,?,?,?,?)", (self.titulo, self.estreno, self.genero, self.duracion, self.director, self.descripcion, self.clasificacion))
        

#peli=Pelicula('El Menú','2022','Thriller',106,'Mark Mylod', 'Una pareja viaja para tener una experiencia culinaria única en el mundo, cuando el ingrediente secreto del platillo preparado por el chef tendrá un resultado sorprendente para la pareja','B-15')
#peli.quitarPelicula(4)
#peli.agregarPelicula()


class Catalogo:
    def __init__(self,peliculas=None):
        self.__peliculas = peliculas

    def listarPeliculas(self):
        conexion = Conexion_BD("BaseDeDatos.db")
        conexion.consulta("SELECT Titulo FROM Peliculas")
        conexion.cerrar()

class Reserva:
    def __init__(self, id_Funcion, id_Cliente):
        self.__id = None
        self.__id_Funcion = id_Funcion
        self.__id_Cliente = id_Cliente
        self.__id_detalle_reservas = None

    @property
    def id(self):
        return self.__id
    @property
    def id_Funcion(self):
        return self.__id_Funcion
    @property
    def id_Cliente(self):
        return self.__id_Cliente
    @property
    def id_detalle_reservas(self):
        return self.__id_detalle_reservas

    @id.setter
    def id(self, nuevoId):
        self.__id = nuevoId
    @id_Funcion.setter
    def id_Funcion(self, nuevoId_Funcion):
        self.__id_Funcion = nuevoId_Funcion
    @id_Cliente.setter
    def id_Cliente(self, nuevoId_Cliente):
        self.__id_Cliente = nuevoId_Cliente
    @id_detalle_reservas.setter
    def id_detalle_reservas(self, nuevoId_Detalle_Reservas):
        self.__id_detalle_reservas = nuevoId_Detalle_Reservas

    def reservar(self):
        conexion = Conexion_BD("BaseDeDatos.db")
        self.id = conexion.insertar("INSERT INTO Reservas(id_Funcion, id_Cliente) VALUES (?,?)", (self.id_Funcion, self.id_Cliente))

    def editReserva(self):
        #conexion = Conexion_BD("BaseDeDatos.db")
        #self.id = conexion.actualizar("UPDATE Reservas SET id_Funcion = ?, id_Cliente =? WHERE ", (self.id_Funcion, self.id_Cliente))
        print(self.id)
    def detallar(self, butacas):
        conexion = Conexion_BD("BaseDeDatos.db")
        self.id_detalle_reservas = conexion.insertar("INSERT INTO Detalle_Reservas(id_Reserva, butacasReservadas) VALUES (?,?)", (self.id, butacas))
    
    def updateDetalle(self, butacas):
        #conexion = Conexion_BD("BaseDeDatos.db")
        #self.id_detalle_reservas = conexion.actualizar("UPDATE Detalle_Reservas SET id_Reserva = ?, butacasReservadas = ? WHERE id = ?", (self.id, butacas, id))
        pass

