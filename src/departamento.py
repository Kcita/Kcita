# -*- coding: utf-8 -*-

codigo_departamento = 0

class Departamento:

    """Este objeto representa un departamento.
        -------------------------------------------
        Atributos:
        - codigo_departamento: integer
        - nombre: string
        - casas: array
        - kcita: object
        -------------------------------------------
        Métodos:
        - agregar_casa(casa)
        - paquetes
        - paquetes_disponibles
    """

    def __init__(self, kcita, nombre = ""):
        """Crea un departamento"""
        global codigo_departamento
        codigo_departamento += 1
        self.codigo_departamento = codigo_departamento
        self.nombre = nombre
        self.casas = []
        self.kcita = kcita
        kcita.agregar_departamento(self)

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "El codigo de departamento es " + str(self.codigo_departamento)+", el nombres es "+str(self.nombre)

    def agregar_casa(self, casa):
        """Recibe dos objetos: Departamento y Casa. Agregar la casa al atributo casas del Departamento."""
        self.casas.append(casa)

    def paquetes(self):
        """Recibe el objeto Departamento y devuelve un array con todos los paquetes en este departamento"""
        paquetes = []
        for casa in self.casas:
            for paquete_de_casa in casa.paquetes_de_casa:
                paquetes.append(paquete_de_casa)
            for dormitorio in casa.dormitorios:
                for paquete_de_dormitorio in dormitorio.paquetes_de_dormitorio:
                    paquetes.append(paquete_de_dormitorio)
        return paquetes

    def paquetes_disponibles(self):
        """Recibe el objeto Departamento y devuelve un array con todos los paquetes disponibles en este departamento"""
        paquetes_disponibles = []
        for casa in self.casas:
            if not casa.dado_de_baja:
                for paquete_de_casa in casa.paquetes_de_casa:
                    paquetes_disponibles.append(paquete_de_casa)
                for dormitorio in casa.dormitorios:
                    for paquete_de_dormitorio in dormitorio.paquetes_de_dormitorio:
                        paquetes_disponibles.append(paquetes_de_dormitorio)
        return paquetes_disponibles
