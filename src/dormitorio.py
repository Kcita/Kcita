# -*- coding: utf-8 -*-

codigo_dormitorio = 0

class Dormitorio:
    """ Este objeto representa una habitación.
        ---------------------------------------------
        Atributos:
        - codigo_dormitorio
        - casa: object
        - tiene_bano_propio: boolean
        - paquetes: array
        ---------------------------------------------
        Métodos:
        - agregar_paquete_dormitorio(paquete_de_dormitorio)
        - reservas
        - propietario
    """

    def __init__(self, casa, numero_camas_sencillas = 0, numero_camas_dobles = 0, tiene_bano_propio = False):
        """Crea un dormitorio"""
        #La varibale codigo_dormitorio es una variable global
        global codigo_dormitorio
        #Se suma un dígito al codigo_dormitorio para que este sea un código único por instancia
        codigo_dormitorio += 1
        self.codigo_dormitorio = codigo_dormitorio
        #Un dormitorio le pertenece a una única casa
        self.casa = casa
        casa.agregar_dormitorio(self)
        self.numero_camas_dobles = numero_camas_dobles
        self.numero_camas_sencillas = numero_camas_sencillas
        self.tiene_bano_propio = tiene_bano_propio
        #Un dormitorio puede alquilarse por paquetes
        self.paquetes_de_dormitorio = []

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "codigo_dormitorio" + str(self.codigo_dormitorio)+ ", numero_de_camas_dobles: " + str(self.numero_camas_dobles) + ", numerocamas_sencillas: " + str(self.numero_camas_sencillas) + ", codigo_casa: " + str(self.casa.codigo_casa)

    def agregar_paquete_de_dormitorio(self, paquete_de_dormitorio):
        self.paquetes_de_dormitorio.append(paquete_de_dormitorio)

    def reservas(self):
        """Devuelve todas las reservas para un dormitorio"""
        reservas = []
        for paquete_de_dormitorio in self.paquetes_de_dormitorio:
            for reserva in paquete_de_dormitorio.reservas:
                reservas.append(reserva)
        return reservas

    def propietario(self):
        """Devuelve el propietario de la casa donde se encuentra el dormitorio"""
        return self.casa.propietario
