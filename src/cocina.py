# -*- coding: utf-8 -*-

codigo_cocina = 0

class Cocina:
    """ Este objeto representa una cocina dentro de una casa.
        ---------------------------------------------
        Atributos:
        - codigo_cocina: integer
        - casa: object
        - tiene_lavavajillas: boolean
        - tiene_lavadoras: boolean
        ---------------------------------------------
        Métodos:
        - agregar_paquete_dormitorio(paquete_de_dormitorio)
        - reservas
        - propietario
    """

    def __init__(self, casa, tiene_lavavajillas, tiene_lavadoras):
        """Crea un dormitorio"""
        #La varibale codigo_cocina es una variable global
        global codigo_cocina
        #Se suma un dígito al codigo_cocina para que este sea un código único por instancia
        codigo_cocina += 1
        self.codigo_cocina = codigo_cocina
        #Una cocina le pertenece a una única casa
        self.casa = casa
        casa.agregar_cocina(self)
        self.tiene_lavavajillas = tiene_lavavajillas
        self.tiene_lavadoras = tiene_lavadoras

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return "codigo_cocina" + str(self.codigo_cocina)+ ", tiene_lavavajillas: " + str(self.tiene_lavavajillas) + ", tiene_lavadoras: " + str(self.tiene_lavadoras) + ", codigo_casa: " + str(self.casa.codigo_casa)
