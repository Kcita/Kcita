# -*- coding: utf-8 -*-

codigo_paquete = 0

class Paquete:

    """Este objeto representa un paquete de alquiler
        -------------------------------------------
        Atributos:
        - codigo_paquete: integer
        - precio_por_dia: float
        - minimo_de_dias: integer
        - titulo: integer
        -------------------------------------------
        Métodos:
        - Propietario: object
    """

    def __init__(self, tipo, precio_por_dia, numero_de_dias, titulo):
        """Crea un paquete"""
        #La variabel codigo_paquete es global
        global codigo_paquete
        #Se suma una unidad al codigo_paquete para que este código sea único
        codigo_paquete += 1
        self.codigo_paquete = codigo_paquete
        #Los paquetes son de dos tipos: Alquiler de habitación en casa o Alquiler de casa completa
        self.tipo = tipo
        #Es el precio por alquiler en un dia
        self.precio_por_dia = precio_por_dia
        #Es el numero de dias por el que se alquila la habitacion o casa en este paquete
        self.numero_de_dias = numero_de_dias
        #Es el título del anuncio que pone el propietario
        self.titulo = titulo
        #Un paquete puede tener varias reservas
        self.reservas = []

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "codigo_paquete: " + str(self.codigo_paquete) + ", tipo: "+ str(self.tipo) + ", precio_por_dia: " + str(self.precio_por_dia) + ", titulo:" + self.titulo
    def agregar_reserva(self, reserva):
        """Recibe el objeto Paquete y el objeto Reserva. Añade la Reserva al atributo reservas"""
        self.reservas.append(reserva)

    def setprecio_por_dia(self, precio_por_dia):
        """Asume precio_por_dia como un float. Establece un nuevo precio por dia del paquete."""
        self.precio_por_dia = precio_por_dia

    def setnumero_de_dias(self, numero_de_dias):
        """Asume numero_de_dias como un integer. Establece un nuevo numero de dias del paquete."""
        self.numero_de_dias = numero_de_dias

class PaqueteCasa(Paquete):
    """Representa un paquete de alquiler de una casa completa"""
    def __init__(self, casa, precio_por_noche, numero_de_dias, titulo):
        """Crea un paquete de casa"""
        #Un paquete de casa le pertence a una única casa
        self.casa = casa
        super().__init__("Casa completa", precio_por_noche, numero_de_dias, titulo)
        casa.agregar_paquete_de_casa(self)

class PaqueteDormitorio(Paquete):
    """Representa un paquete de alquiler de un dormitorio en una casa"""
    def __init__(self, dormitorio, precio_por_noche, numero_de_dias, titulo):
        """Crea un paquete de dormitorio"""
        #Un paquete de dormitorio le pertenece a un único dormitorio.
        self.dormitorio = dormitorio
        super().__init__("Habitación", precio_por_noche, numero_de_dias, titulo)
        dormitorio.agregar_paquete_de_dormitorio(self)