# -*- coding: utf-8 -*-

codigo_propietario = 0

class Propietario:

    """Este objeto representa un propietario que pone su o sus casas en alquiler.
        -------------------------------------------
        Atributos:
        - codigo_propietario: integer
        - usuario: string
        - password: string
        - nombre: string
        - kcita: object
        - casas: array
        - mail: string
        - sesion_iniciada: boolean
        -------------------------------------------
        Métodos:
        - Agregar_casa
        - Paquetes
    """

    def __init__(self, kcita, usuario, password, nombre):
        """Crea un propietario"""
        #El codigo_propietario es una variable con scope global.
        global codigo_propietario
        #Se suma una unidad al código de propietario para generarlo automáticamente.
        codigo_propietario += 1
        self.codigo_propietario = codigo_propietario
        #El atributo casas son las casas que tiene este propietario
        self.casas = []
        #El nombre de usuario no distingue entre mayusculas y minusculas, y es un campo unico.
        usuario = usuario.lower()
        #Mientras el nombre de usuario se siga repitiendo, se pedirá que se intente con otro nombre
        while usuario in kcita.nombres_de_usuarios_ocupados():
            #Un nombre de usuario es válido si no se ha creado uno igual anteriormente.
            usuario = input("Nombre de usuario ocupado. Pruebe con otro nombre de usuario: ")
            usuario = usuario.lower()
        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.kcita = kcita
        kcita.agregar_propietario(self)
        self.sesion_iniciada = False

    def __str__():
        """Devuelve una representación de caractéres de self"""
        return "el usario es " + str(self.usuario)+", el passwoerd es "+ str(self.password)+", el nombre es "+str(self.nombre)

    def cambiar_password(self, antiguo_password, nuevo_password):
        """Recibe el objeto Propietario, un password original y un password nuevo"""
        #se debe verificar que la contraseña antigua es igual a la contraseña original
        if self.password == antiguo_password:
            #si se cumple, se cambia la contraseña
            self.password = nuevo_password
            print("Contraseña cambiada")
        else:
            print("Contraseña antigua no coincide.")

    def agregar_casa(self, casa):
        """Recibe el objeto Propietario y el objeto casa. Agrega la casa al atributo Casas del Propietario."""
        self.casas.append(casa)

    def inicio_sesion(self):
        """Se inicia la sesión de este propietario"""
        self.sesion_iniciada = True

    def cerrar_sesion(self):
        """Se cierra la sesión de este propietario"""
        self.sesion_iniciada = False
