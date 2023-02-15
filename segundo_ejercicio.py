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
    
    def ingresarPaciente(self):
        
        nombre = input("Ingrese el Nombre: ")
        cedula = int(input("Ingrese la Cédula: "))
        genero = input("Ingrese el Género: ")
        servicio = input("Ingrese el Servicio: ")
        
        paciente = Paciente()
        paciente.asignarNombre(nombre)
        paciente.asignarCedula(cedula)
        paciente.asignarGenero(genero)
        paciente.asignarServicio(servicio)
        
        self.__lista_pacientes.append(paciente)
        self.__numero_pacientes = len(self.__lista_pacientes)  

    def ver_numeroPacientes(self):
        return self.__numero_pacientes
    
    def verDatosPacientes(self):
        cedula = int(input("Ingrese la Cédula a buscar: "))
        #Es for paciente y no cedula porque en la lista hay pacientes no numeros 
        for paciente in self.__lista_pacientes: 
            if cedula == paciente.verCedula():
                print("Nombre: " + paciente.verNombre())
                print("Cédula: " + str(paciente.verCedula()))
                print("Género: " + paciente.verGenero())
                print("Servicio: " + paciente.verServicio())   

sistema = Sistema()



while True:
    
    menu = int(input('''
                 *** SELECCIONE UNA OPCION DEL MENU***
                 1. Ingresar paciente.
                 2. Numero de pacientes.
                 3. Datos de paciente.
                 4. Salir.
                 ----> '''))
    
    if menu == 1:
        sistema.ingresarPaciente()
    
    elif menu == 2:
        print('El numero total de pacientes es: ' + str(sistema.ver_numeroPacientes()))
    
    elif menu == 3:
        sistema.verDatosPacientes()
    
    elif menu == 4:
        break
    
    else:
        print('<<Opcion no valida>>')