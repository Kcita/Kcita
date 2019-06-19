# -*- coding: utf-8 -*-

codigo_casa = 0

class Casa:

    """Este objeto representa una casa.
        --------------------------------
        Atributos:
        - codigo_casa: integer
        - propietario: object
        - departamento = object
        - direccion: string
        - numero_dormitorios: integer
        - numero_banos: integer
        - numero_cocinas: integer
        - numero_comedores: integer
        - numero_plazas_garaje: integer
        - descripcion_general: string
        - dado_de_baja: boolean
        - valido: boolean
        - dormitorios: array
        Métodos:
    """

    def __init__(self,propietario, departamento, direccion = "", numero_dormitorios = 0, numero_banos = 0, numero_cocinas = 0, numero_comedores = 0, numero_plazas_garaje = 0, descripcion_general = ""):
        """Crea una casa"""
        #La variable codigo casa es una variable global
        global codigo_casa
        #Se suma una unidad al codigo_casa para que este código sea único
        codigo_casa += 1
        self.codigo_casa = codigo_casa
        #Una casa le pertence a un único propietario
        self.propietario = propietario
        propietario.agregar_casa(self)
        #Una casa le pertenece a un único departamento
        self.departamento = departamento
        departamento.agregar_casa(self)
        self.direccion = direccion
        self.numero_dormitorios = numero_dormitorios
        self.numero_comedores = numero_comedores
        self.numero_cocinas = numero_cocinas
        self.numero_banos = numero_banos
        self.numero_plazas_garaje = numero_plazas_garaje
        self.descripcion_general = descripcion_general
        #Una casa tiene varios dormitorios
        self.dormitorios = []
        self.departamento = departamento
        departamento.agregar_casa(self)
        #Una casa tiene varios paquetes
        self.paquetes_de_casa = []
        #Una casa es válida si cuenta con al menos una cocina, 3 habitaciones y 2 baños
        """if numero_dormitorios <= 3 and numero_cocinas <= 1 and numero_banos <= 2:
            raise ValueError"""
        self.valido = True
        self.dado_de_baja = False

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "Codigo de casa" + str(self.codigo_casa)+ ", " + "la direccion es " + str(self.direccion)+ ", " + "el numero de dormitorios es "+ str(self.numero_dormitorios)+ ", " + "el numero de cocinas es " + str(self.numero_cocinas) + ", "+ "el numero de comedores es " + str(self.numero_comedores)+ " y el numero de baños es "+str(self.numero_banos)

    def agregar_dormitorio(self, dormitorio):
        self.dormitorios.append(dormitorio)

    def agregar_paquete_de_casa(self, paquete_de_casa):
        """Agrega un paquete de casa a la casa"""
        self.paquetes_de_casa.append(paquete_de_casa)

    def dar_de_baja(self):
        """Recibe el objeto Casa y cambia el atributo Dado_de_baja a True"""
        self.dado_de_baja = True
