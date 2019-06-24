# -*- coding: utf-8 -*-

import datetime

class Kcita:

    """Representa la plataforma de gestión de reserva de alquileres
        Atributos:
        - Propietarios
        - Clientes
        - Departamentos
        -------------------------------------------
        Métodos:
        - agregar_propietario
        - agregar_cliente
        - agregar_departamento
        - reservas
        - casas
        - dormitorios
        - paquetes
        - nombres_de_usuarios_ocupados
        - iniciar_sesion
    """

    def __init__(self, nombre):
        """Crea una Kcita"""
        self.nombre = nombre
        #En el sistema hay varios propietarios
        self.propietarios = []
        #En el sistema hay varios clientes
        self.clientes = []
        #En el sistema hay varios departamentos
        self.departamentos = []
        #Por defecto, ningún propietario ha iniciado sesión
        self.sesion_iniciada = False

    def __str__(self):
        """Devuelve una representación de caractéres de self"""
        return str(self.nombre)

    def agregar_propietario(self, propietario):
        """Recibe dos objetos: Kcita y Propietario. Agrega el Propietario al atributo propietarios."""
        self.propietarios.append(propietario)

    def agregar_cliente(self, cliente):
        """Recibe dos objetos: Kcita y Cliente. Agrega el Cliente al atributo clientes."""
        self.clientes.append(cliente)

    def agregar_departamento(self, departamento):
        """Recibe dos objetos: Departamento y Propietario. Agrega el Departamento al atributo departamentos."""
        self.departamentos.append(departamento)

    def reservas(self):
        """Recibe el objeto Kcita. Devuelve un array con todas las reservas en el sistema."""
        reservas = []
        for cliente in self.clientes:
            for reserva in cliente.reservas:
                reservas.append(reserva)
        return reservas

    def casas(self):
        """Recibe el objeto Kcita. Devuelve un array con todas las casas en el sistema."""
        casas = []
        for propietario in self.propietarios:
            for casa in propietario.casas:
                casas.append(casa)
        return casas

    def dormitorios(self):
        """Recibe el objeto Kcita. Devuelve un array con todos los dormitorios en el sistema"""

        dormitorios = []

        for propietario in self.propietarios:
            #Un propietario puede tener muchas casas
            for casa in propietario.casas:
                #En una casa pueden haber 0 o varios dormitorios
                for dormitorio in casa.dormitorios:
                    dormitorios.append(dormitorio)

        return dormitorios

    def paquetes(self):
        """Recibe el objeto Kcita. Devuelve un array con todos los objetos"""

        paquetes = []

        for propietario in self.propietarios:
            for casa in propietario.casas:
                for paquete_de_casa in casa.paquetes_de_casa:
                    paquetes.append(paquete_de_casa)
                for dormitorio in casa.dormitorios:
                    for paquete_de_dormitorio in casa.paquetes_de_dormitorio:
                        paquetes.append(paquete_de_dormitorio)

        return paquetes

    def nombres_de_usuarios_ocupados(self):
        """Devuelve una lista con los nombres de usuario que ya están siendo usados"""
        nombres_de_usuarios_ocupados = []
        for propietario in self.propietarios:
            nombres_de_usuarios_ocupados.append(propietario.usuario)
        return nombres_de_usuarios_ocupados

    def iniciar_sesion(self, usuario, password):
        """Recibe Kcita de objeto, usuario de string y password de string.
            Si el usuario y password es correcto, se inicia una sesión en el sistema y devuelve True."""
        if not self.sesion_iniciada:
            for propietario in self.propietarios:
                if propietario.usuario == usuario and propietario.password == password:
                    propietario.inicio_sesion()
                    self.sesion_iniciada = True
                    print("Inicio de sesión satisfactorio")
                    return True
            if not self.sesion_iniciada:
                print("Nombre de usuario y contraseña no coinciden.")
                return False
        else:
            print("Ya tiene una sesión abierta")
            return False

    def salir_sesion(self):
        """Cierra la sesión en el sistema y de cualquier usuario que haya ingresado al sistema"""
        self.sesion_iniciada = False
        for propietario in self.propietarios:
            propietario.sesion_iniciada = False


    def busqueda_por_codigo_de_casa(self, codigo_casa):
        """Recibe un código de casa (int) y devuelve los paquetes que hay en esta casa"""
        #Se asume que la busqueda es inválida
        busqueda_valida = False

        for casa in self.casas():
            #El código de la Casa es único y debe coincidir. Además, la Casa no debe haber sido dado de baja por el Propietario.
            if casa.codigo_casa == codigo_casa and not casa.dado_de_baja:
                #Hay una única casa a la cual le corresponde el código
                casaRef = casa
                #Si se encuentra una casa, la busqueda es válida
                busqueda_valida += True
                break
        if busqueda_valida:
            return casa.paquetes()
        else:
            print("Ninguna casa coincide con este código o la casa fue dada de baja.")

    def busqueda_de_departamento_por_codigo(self, codigo_departamento):
        for departamento in self.departamentos:
            if departamento.codigo_departamento == codigo_departamento:
                return departamento

    def busqueda_de_propietario_por_usuario(self, usuario):
        for propietario in self.propietarios:
            if propietario.usuario == usuario:
                return propietario

    def busqueda_de_cliente_por_celular(self, celular):
        for cliente in self.clientes:
            if cliente.celular == celular:
                return cliente

    def busqueda_de_casa_por_codigo(self, codigo_casa):
        for casa in self.casas():
            if casa.codigo_casa == codigo_casa:
                return casa

    def busqueda_de_paquete_por_codigo(self, codigo_paquete):
        for paquete in self.paquetes():
            if paquete.codigo_paquete == codigo_paquete:
                return paquete

    def busqueda(self, codigo_casa, dia_de_entrada, numero_de_noches):
        """Recibe un código de casa (int), un dia de entrada (datetime.date) y un numero de noches (int).
            Devuelve un array de paquetes o un mensaje de error (str)"""

        busqueda_valida = False

        for casa in self.casas():
            #El código de la Casa es único y debe coincidir. Además, la Casa no debe haber sido dado de baja por el Propietario.
            if casa.codigo_casa == codigo_casa and not casa.dado_de_baja:
                #Hay una única casa a la cual le corresponde el código
                casaRef = casa
                #Si se encuentra una casa, la busqueda es válida
                busqueda_valida += True
                break

        if not busqueda_valida:
            return []
        else:
            paquetes_disponibles = []
            for paquete_de_casa in casaRef.paquetes_de_casa:
                paquete_esta_disponible = True
                for reserva in paquete_de_casa.reservas:
                    dias_que_se_quieren_reservar = []
                    for i in range(0, numero_de_noches + 1):
                        dias_que_se_quieren_reservar.append(dia_de_entrada + datetime.timedelta(days = i))
                    for dia_que_se_quiere_reservar in dias_que_se_quieren_reservar:
                        for dia_ya_reservado in reserva.dias:
                            if dia_que_se_quiere_reservar == dia_ya_reservado:
                                paquete_esta_disponible = False
                                break
                if paquete_esta_disponible:
                    paquetes_disponibles.append(paquete_de_casa)

            for dormitorio in casaRef.dormitorios:
                for paquete_de_dormitorio in dormitorio.paquetes_de_dormitorio:
                    paquete_esta_disponible = True
                    for reserva in paquete_de_dormitorio.reservas:
                        dias_que_se_quieren_reservar = []
                        for i in range(0, numero_de_noches + 1):
                            dias_que_se_quieren_reservar.append(dia_de_entrada + datetime.timedelta(days = i))
                        for dia_que_se_quiere_reservar in dias_que_se_quieren_reservar:
                            for dia_ya_reservado in reserva.dias:
                                if dia_que_se_quiere_reservar == dia_ya_reservado:
                                    paquete_esta_disponible = False
                                    break
                    if paquete_esta_disponible:
                        paquetes_disponibles.append(paquete_de_dormitorio)

        return paquetes_disponibles

    def busqueda_por_atributo(atributo, valor):

        """Recibe un atributo de la casa y su valor. Devuelve los paquetes que cumplen con este atributo"""

        paquetes = []

        if atributo == "Número de dormitorios":
            for casa in self.casas:
                if casa.numero_dormitorios >= valor:
                    for paquete in casa.paquetes():
                        paquetes.append(paquete)
        if atributo == "Número de baños":
            for casa in self.casas:
                if casa.numero_banos >= valor:
                    for paquete in casa.paquetes():
                        paquetes.append(paquete)
        if atributo == "Numero de cocinas":
            for casa in self.casas:
                if casa.numero_cocinas >= valor:
                    for paquete in casa.paquetes():
                        paquetes.append(paquete)
