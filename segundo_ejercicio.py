class Paciente():
    
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
        self.__servicio = ""
    
    # Getters

    def asignarNombre(self, nombre):
        self.__nombre = nombre
    
    def asignarCedula(self, cedula):
        self.__cedula = cedula

    def asignarGenero(self, genero):
        self.__genero = genero

    def asignarServicio(self, servicio):
        self.__servicio = servicio
    
    # Setters

    def verNombre(self):
        return self.__nombre
    
    def verCedula(self):
        return self.__cedula
    
    def verGenero(self):
        return self.__genero
    
    def verServicio(self):
        return self.__servicio

class Sistema():

    def __init__(self):
        self.__lista_pacientes = []

        self.__numero_pacientes = len(self.__lista_pacientes)
        