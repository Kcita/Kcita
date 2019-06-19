# -*- coding: utf-8 -*-

codigo_pago = 0

import datetime

class Pago:
    """Representa el pago que hace un cliente a un propietario por la reserva"""
    def __init__(self, reserva, monto, fecha = datetime.date.today()):
        """Crea un pago"""
        #El codigo_pago es una variable global
        global codigo_pago
        codigo_pago += 1
        self.codigo_pago = codigo_pago
        #Un pago corresponde a una única reserva
        self.reserva = reserva
        #Una reserva tiene varios pagos:
        reserva.agregar_pago(self)
        #Un pago debe tener un monto específico
        self.monto = monto
        #Se debe verificar que el pago es un número mayor a cero
        while monto < 0:
            monto = float(input("Cantidad inválida, introduzca un número mayor a cero: "))
            self.monto = monto
        #Un pago se hace en una fecha en específico
        self.fecha = fecha

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "codigo_pago: " + str(self.codigo_pago) + ", codigo_reserva: " + str(self.reserva.codigo_reserva) + ", monto: " + str(self.monto) + ", fecha: " + str(self.fecha)
