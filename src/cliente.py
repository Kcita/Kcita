# -*- coding: utf-8 -*-

codigo_cliente = 0

class Cliente:

    """Este objeto representa un cliente que va a alquilar una casa
        -------------------------------------------
        Atributos:
        - Nombre: string
        - Celular: string
        - Mail: string
        - Reservas: array
        -------------------------------------------
        Métodos:
        -
        """
    def __init__(self, kcita, nombre, celular, mail):
        """Crea un cliente"""
        global codigo_cliente
        codigo_cliente += 1
        self.codigo_cliente = codigo_cliente
        self.nombre = nombre
        self.celular = celular
        self.mail = mail
        self.reservas = []
        self.kcita = kcita
        kcita.agregar_cliente(self)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "cliente:"+str(self.nombre)+"/ celular"+str(self.celular)