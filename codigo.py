# -*- coding: utf-8 -*-
codigo_departamento = 0
codigo_reserva = 0
codigo_paquete = 0
codigo_cliente = 0
codigo_propietario = 0
codigo_casa = 0
codigo_dormitorio = 0

import datetime

class Departamento:

    """Este objeto representa un departamento.
        -------------------------------------------
        Atributos:
        - Codigo_departamento: integer
        - Nombre: string
        - Casas: array
        -------------------------------------------
        Métodos:
        - Agregar_casa
        - Mostrar_casas
        - Paquetes
    """

    def __init__(self, kcita, nombre = ""):
        global codigo_departamento
        codigo_departamento += 1
        self.codigo_departamento = codigo_departamento
        self.nombre = nombre
        self.casas = []
        self.paquetes = []
        self.kcita = kcita
        kcita.agregar_departamento(self)

    def __str__(self):
        return "El codigo de departamento es " + str(self.codigo_dormitorio)+", el nombres es "+str(self.nombre)

    def agregar_casa(self, casa):
        self.casas.append(casa)

    def paquetes(self):
        pass

class Propietario:

    """Este objeto representa un propietario que pone su o sus casas en alquiler
        -------------------------------------------
        Atributos:
        - Usuario: string
        - Password: string
        - Casas: array
        -------------------------------------------
        Métodos:
        - Agregar_casa
        - Agregar_casa
        - Paquetes
    """

    def __init__(self, kcita, usuario, password, nombre):
        global codigo_propietario
        codigo_propietario += 1
        self.casas = []
        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.codigo_propietario=codigo_propietario
        self.kcita = kcita
        kcita.agregar_propietario(self)

    def __str__():
        return "el usario es " + str(self.usuario)+", el passwoerd es "+ str(self.password)+", el nombre es "+str(self.nombre)

    def cambiar_password(self, antiguo_password, nuevo_password):
        if self.password == antiguo_password:
            self.password = nuevo_password


    def agregar_casa(self, casa):
        self.casas.append(casa)
        pass

    def paquetes(self):
        pass


class Casa:
    """Este objeto representa una casa.
        --------------------------------
        Atributos:
        - Codigo de casa: integer
        - Direccion: string
        - Dormitorios: array
        - Numero_dormitorios: integer
        - Numero_baños: integer
        - Numero_comedores: integer
        - Numero_cocinas: integer
        Métodos:
        -
        -
    """

    def __init__(self, kcita, propietario, departamento, direccion = "", numero_dormitorios = 0, numero_cocinas = 0, numero_banos = 0, numero_comedores = 0):
        #Una casa le pertence a un único cliente
        self.propietario = propietario
        self.direccion = direccion
        self.numero_dormitorios = numero_dormitorios
        self.numero_comedores = numero_comedores
        self.numero_cocinas = numero_cocinas
        self.numero_banos = numero_banos
        global codigo_casa
        codigo_casa += 1
        self.codigo_casa = codigo_casa
        self.dormitorios = []
        self.departamento = departamento
        propietario.agregar_casa(self)
        self.paquetes_de_casa=[]
        self.kcita = kcita
        kcita.agregar_casa(self)


    def __str__(self):
        return "Codigo de casa" + str(self.codigo_casa)+ ", " + "la direccion es " + str(self.direccion)+ ", " + "el numero de dormitorios es "+ str(self.numero_dormitorios)+ ", " + "el numero de cocinas es " + str(self.numero_cocinas) + ", "+ "el numero de comedores es " + str(self.numero_comedores)+ " y el numero de baños es "+str(self.numero_banos)


    def agregar_dormitorio(self, dormitorio):
        self.dormitorios.append(dormitorio)

    def agregar_paquetes_casa(self, paquete_casa):
        self.paquetes_de_casa.append(paquete_casa)


class Dormitorio:
    """ Este objeto representa una habitación.
        ---------------------------------------------
        Atributos:
        - Casa: object
        -
        ---------------------------------------------
        Métodos:
        -
    """

    def __init__(self, kcita, casa, numerocamas_sencillas = 0, numerocamas_dobles = 0):

        global codigo_dormitorio
        codigo_dormitorio += 1
        self.codigo_dormitorio = codigo_dormitorio
        self.numerocamas_dobles = numerocamas_dobles
        self.numerocamas_sencillas = numerocamas_sencillas
        self.casa = casa
        casa.agregar_dormitorio(self)
        self.paquetes_de_dormitorio=[]
        self.kcita = kcita
        kcita.agregar_dormitorio(self)

    def __str__(self):
        return "el codigo de dormitorio"+str(self.codigo_dormitorio)+", "+ "el numero de camas dobles"+str(self.codigo_dormitorio)+", "+"numero de camas simples"+str(self.numerocamas_sencillas)+"| numero_banos: "+str(self.casa.numero_banos)

    def agregar_paquete_dormitorio(self, dormitorio):
        self.paquetes_de_dormitorio.append(dormitorio)

class Paquete:

    """Este objeto representa un paquete de alquiler
        -------------------------------------------
        Atributos:
        - Codigo_paquete: integer
        - Precio_por_noche: float
        - Casa: object
        -------------------------------------------
        Métodos:
        - Propietario: object
    """

    def __init__(self, tipo, precio_por_noche, descripcion):
        global codigo_paquete
        codigo_paquete += 1
        self.codigo_paquete = codigo_paquete
        self.tipo = tipo
        self.precio_por_noche = precio_por_noche
        self.descripcion = descripcion
        self.reservas = []

    def __str__(self):
        return "codigo_paquete: " + str(self.codigo_paquete) + ", tipo: "+ str(self.tipo) + ", precio_por_noche: " + str(self.precio_por_noche) + ", descripcion:" + self.descripcion

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

class Paquete_de_casa(Paquete):
    def __init__(self, casa, precio_por_noche, descripcion):
        self.casa = casa
        self.kcita = casa.kcita
        self.kcita.agregar_paquete(self)
        super().__init__("Casa completa", precio_por_noche, descripcion)
        casa.agregar_paquetes_casa(self)

class Paquete_de_dormitorio(Paquete):
    def __init__(self, dormitorio, precio_por_noche, descripcion):
        self.dormitorio = dormitorio
        self.kcita = dormitorio.kcita
        self.kcita.agregar_paquete(self)
        super().__init__("Por habitación", precio_por_noche, descripcion)
        dormitorio.agregar_paquete_dormitorio(self)

class Reserva:

    """Este objeto representa la reserva de un paquete de alquiler
        Atributos:
        - Código_de_reserva: integer
        - Paquete: object
        - Fecha de reserva: datetime
        - Fecha de inicio: datetime
        - Precio: atributo
        ----------------------------------------------------------
        Métodos:
        - Casa
        - Habitacion
        """

    def __init__(self, kcita, cliente, paquete, fecha_de_inicio_de_reserva, fecha_de_fin_de_reserva):
        global codigo_reserva
        codigo_reserva += 1
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.paquete = paquete
        self.fecha_de_inicio_de_reserva = fecha_de_inicio_de_reserva
        self.fecha_de_fin_de_reserva = fecha_de_fin_de_reserva
        self.numero_de_noches = fecha_de_fin_de_reserva - fecha_de_inicio_de_reserva
        self.precio_total = self.numero_de_noches * paquete.precio_por_noche
        self.kcita = kcita
        kcita.agregar_reserva(self)
        paquete.agregar_reserva(self)

    def __str__(self):
        return "Cliente: " + str(self.cliente) + "/ paquete" +str(self.paquete)+ "/ fecha_de_fin_de_reserva" + str(self.fecha_de_fin_de_reserva)+"/ fecha fecha_de_inicio_de_reserva"+str(self.fecha_de_inicio_de_reserva) + "numero_de_noches: " + str(self.numero_de_noches) + "precio_total: " + str(self.precio_total)

class Cliente:

    """Este objeto representa un cliente que va a alquilar una casa
        -------------------------------------------
        Atributos:
        - Nombre: string
        - Celular: string
        - Reservas: array
        -------------------------------------------
        Métodos:
        -
        """
    def __init__(self, kcita, nombre, celular):
        global codigo_cliente
        codigo_cliente += 1
        self.codigo_cliente = codigo_cliente
        self.nombre = nombre
        self.celular = celular
        self.reservas = []
        self.kcita = kcita
        kcita.agregar_cliente(self)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def __str__(self):
        return "cliente:"+str(self.nombre)+"/ celular"+str(self.celular)


class Kcita():

    def __init__(self, nombre):
        self.nombre = nombre
        self.casas = []
        self.departamentos = []
        self.clientes = []
        self.propietarios = []
        self.reservas = []
        self.paquetes = []
        self.dormitorios=[]

    def agregar_casa(self, casa):
        self.casas.append(casa)

    def agregar_dormitorio(self, dormitorio):
        self.dormitorios.append(dormitorio)

    def agregar_propietario(self,propietario):
        self.propietarios.append(propietario)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def agregar_departamento(self, departamento):
        self.departamentos.append(departamento)

    def agregar_paquete(self,paquete):
        self.paquetes.append(paquete)

    def agregar_reserva(self,reserva):
        self.reservas.append(reserva)

    def __str__(self):
            return str(self.nombre)


def test():

    kcita = Kcita("Kcita")

    departmento = Departamento(kcita, "Lima")
    departmento2 = Departamento(kcita, "Arequipa")
    departmento3 = Departamento(kcita, "Huancayo")
    print(departmento.codigo_departamento)
    print(departmento2.codigo_departamento)
    print(departmento3.codigo_departamento)

    cliente1 = Cliente(kcita, "Renato Palomino", "938618324")
    cliente2 = Cliente(kcita, "Sebastian Ramos", "978762123")
    propietario1 = Propietario(kcita, "paolo_bejarano", "12345", "Paolo Bejarano")
    propietario2 = Propietario(kcita, "carrrdenas", "bea", "Alvaro Cardenas")
    casa = Casa(kcita, propietario1, departmento, "Av. Parque Las leyendas, San Miguel", 2, 1, 1, 1)
    casa2 = Casa(kcita, propietario1, departmento, "Av. Reducto, San Miguel", 2, 1, 1, 1)
    dormitorio = Dormitorio(kcita, casa2, 1, 2)

    paquete1 = Paquete_de_casa(casa, 30.0, "Casa en alquiler")
    print(paquete1)
    print(paquete1.casa)
    paquete2 = Paquete_de_dormitorio(dormitorio, 15.0, "Departamento en alquiler")
    print(paquete2)
    print(paquete2.dormitorio)

    reserva1 = Reserva(kcita, cliente1, paquete1, datetime.date(2019, 6, 21), datetime.date(2019, 6, 24))
    print(reserva1)
    print(reserva1.paquete)
    print(paquete1.reservas)
    reserva2 = Reserva(kcita, cliente2, paquete2, datetime.date(2019, 6, 22), datetime.date(2019, 6, 25))
    print(reserva2)

    print(kcita.reservas)
    print(kcita.casas)
    print(kcita.dormitorios)
    print(kcita.paquetes)
    print(kcita.departamentos)
    print(kcita.clientes)
    print(kcita.propietarios)

test()
