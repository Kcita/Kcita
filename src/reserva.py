# -*- coding: utf-8 -*-

import datetime

codigo_reserva = 0

class Reserva:

    """Este objeto representa la reserva de un paquete de alquiler
        Atributos:
        - codigo_reserva: integer
        - cliente: object
        - paquete: object
        - fecha_de_creacion: datetime
        - fecha_de_inicio_de_reserva: datetime
        - fecha_de_fin_de_reserva: datetime
        - precio_total: float
        - pago_atrasado: boolean
        - anulado: boolean
        - pagos: array
        ----------------------------------------------------------
        Métodos:
        - numero_de_noches
        - monto_cobrado
        - adelanto_esta_atrasado
        - pagado
        """

    def __init__(self, cliente, paquete, fecha_de_creacion, fecha_de_inicio_de_reserva):
        """Crea una reserva"""
        global codigo_reserva
        codigo_reserva += 1
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.paquete = paquete
        self.fecha_de_creacion = fecha_de_creacion
        self.fecha_de_inicio_de_reserva = fecha_de_inicio_de_reserva
        self.fecha_de_fin_de_reserva = fecha_de_inicio_de_reserva + datetime.timedelta(days = paquete.numero_de_dias - 1)
        self.numero_de_noches = (self.fecha_de_fin_de_reserva - self.fecha_de_inicio_de_reserva).days
        self.precio_total = paquete.numero_de_dias * paquete.precio_por_dia
        self.pago_atrasado = False
        self.dias = []
        for i in range(0, self.numero_de_noches + 1):
            self.dias.append(self.fecha_de_inicio_de_reserva + datetime.timedelta(days = i))
        paquete.agregar_reserva(self)
        self.pagos = []

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "codigo_reserva: " + str(self.codigo_reserva) + ", codigo_paquete:" +str(self.paquete.codigo_paquete) + ", estado: " + ", fecha_de_inicio_de_reserva: " + str(self.fecha_de_inicio_de_reserva) + ", fecha_de_fin_de_reserva:" + str(self.fecha_de_fin_de_reserva) + ", numero_de_noches: " + str(self.numero_de_noches) + ", precio_total: " + str(self.precio_total)

    def agregar_pago(self, pago):
        """Agrega un pago al atributo pagos"""
        self.pagos.append(pago)

    def monto_cobrado(self):
        """Calcula el monto cobrado a la actualidad"""
        monto_cobrado = 0
        for pago in self.pagos:
            monto_cobrado += pago.monto
        return monto_cobrado

    def anular(self):
        """Cambia el atributo anulado a True"""
        self.anulado = True

    def adelanto_esta_atrasado(self):
        """Devuelve True si el pago está atrasado, devuelve False caso contrario"""
        hoy_dia = datetime.date.today()
        if (hoy_dia - self.fecha_de_creacion).days >= 3 and self.monto_cobrado <= 0.2 * self.precio_total:
            return True
        else:
            return False

    def pagado(self):
        """Devuelve True si la reserva ha sido pagada, devuelve False caso contrario"""
        if self.monto_cobrado() == self.precio_total:
            return True
        else:
            return False
        
