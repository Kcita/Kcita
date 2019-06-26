# -*- coding: utf-8 -*-

codigo_cliente = 0

class Cliente:

    """Este objeto representa un cliente que va a alquilar una casa
        -------------------------------------------
        Atributos:
        - codigo_cliente: integer
        - nombre: string
        - celular: string
        - mail: string
        - reservas: array
        - kcita: object
        -------------------------------------------
        Métodos:
        - agregar_reserva(reserva)
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

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "cliente:"+str(self.nombre)+"/ celular"+str(self.celular)

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
