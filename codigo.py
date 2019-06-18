# -*- coding: utf-8 -*-
codigo_departamento = 0
codigo_reserva = 0
codigo_paquete = 0
codigo_cliente = 0
codigo_propietario = 0
codigo_casa = 0
codigo_dormitorio = 0

#Libreria para uso de fechas
import datetime
#Libreria Tkinter para interfaz gráfica.
from tkinter import *
from tkinter import ttk

class Departamento:

    """Este objeto representa un departamento.
        -------------------------------------------
        Atributos:
        - Codigo_departamento: integer
        - Nombre: string
        - Casas: array
        - Kcita: object
        -------------------------------------------
        Métodos:
        - Agregar_casa
        - Paquetes
    """

    def __init__(self, kcita, nombre = ""):
        """Creacion de un departamento nuevo"""
        global codigo_departamento
        codigo_departamento += 1
        self.codigo_departamento = codigo_departamento
        self.nombre = nombre
        self.casas = []
        self.kcita = kcita
        kcita.agregar_departamento(self)

    def __str__(self):
        return "El codigo de departamento es " + str(self.codigo_dormitorio)+", el nombres es "+str(self.nombre)

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

class Propietario:

    """Este objeto representa un propietario que pone su o sus casas en alquiler.
        -------------------------------------------
        Atributos:
        - Usuario: string
        - Password: string
        - Casas: array
        - Mail: string
        - Inicio_sesion: boolean
        -------------------------------------------
        Métodos:
        - Agregar_casa
        - Paquetes
    """

    def __init__(self, kcita, usuario, password, nombre):
        #El codigo_propietario es una variable con scope global.
        global codigo_propietario
        #Se suma una unidad al código de propietario para generarlo automáticamente.
        codigo_propietario += 1
        self.codigo_propietario=codigo_propietario
        #El atributo casas son las casas que tiene este propietario
        self.casas = []
        #El nombre de usuario no distingue entre mayusculas y minusculas, y es un campo unico.
        usuario = usuario.lower()
        #Un nombre de usuario es válido si no se ha creado uno igual anteriormente.
        nombres_de_usuarios_ocupados = kcita.nombres_de_usuarios_ocupados()
        #Mientras el nombre de usuario se siga repitiendo, se pedirá que se intente con otro nombre
        while usuario in nombres_de_usuarios_ocupados:
            usuario = input("Nombre de usuario ocupado. Pruebe con otro nombre de usuario: ")
            usuario = usuario.lower()
        self.usuario = usuario
        self.password = password
        self.nombre = nombre
        self.kcita = kcita
        #El usuario inicia sesión apenas se registre
        self.sesion_iniciada = True
        kcita.agregar_propietario(self)

    def __str__():
        return "el usario es " + str(self.usuario)+", el passwoerd es "+ str(self.password)+", el nombre es "+str(self.nombre)

    def cambiar_password(self, antiguo_password, nuevo_password):
        """Recibe el objeto Propietario, un password original y un password nuevo"""
        if self.password == antiguo_password:
            self.password = nuevo_password
            print("Contraseña cambiada")
        else:
            print("Contraseña antigua no coincide.")

    def agregar_casa(self, casa):
        """Recibe el objeto Propietario y el objeto casa. Agrega la casa al atributo Casas del Propietario."""
        self.casas.append(casa)

class Casa:

    """Este objeto representa una casa.
        --------------------------------
        Atributos:
        - codigo_casa: integer
        - propietario: object
        - departamento = object
        - direccion: string
        - numero_dormitorios: integer
        - numero_banos: integer
        - numero_cocinas: integer
        - numero_comedores: integer
        - numero_plazas_garaje: integer
        - descripcion_general: string
        - dado_de_baja: boolean
        - valido: boolean
        - dormitorios: array
        Métodos:
    """

    def __init__(self,propietario, departamento, direccion = "", numero_dormitorios = 0, numero_banos = 0, numero_cocinas = 0, numero_comedores = 0, numero_plazas_garaje = 0, descripcion_general = ""):
        #La variable codigo casa es una variable global
        global codigo_casa
        #Se suma una unidad al codigo_casa para que este código sea único
        codigo_casa += 1
        self.codigo_casa = codigo_casa
        #Una casa le pertence a un único propietario
        self.propietario = propietario
        propietario.agregar_casa(self)
        #Una casa le pertenece a un único departamento
        self.departamento = departamento
        departamento.agregar_casa(self)
        self.direccion = direccion
        self.numero_dormitorios = numero_dormitorios
        self.numero_comedores = numero_comedores
        self.numero_cocinas = numero_cocinas
        self.numero_banos = numero_banos
        self.numero_plazas_garaje = numero_plazas_garaje
        self.descripcion_general = descripcion_general
        #Una casa tiene varios dormitorios
        self.dormitorios = []
        self.departamento = departamento
        departamento.agregar_casa(self)
        #Una casa tiene varios paquetes
        self.paquetes_de_casa = []
        #Una casa es válida si cuenta con al menos una cocina, 3 habitaciones y 2 baños
        if numero_dormitorios <= 3 and numero_cocinas <= 1 and numero_banos <= 2:
            raise ValueError
        self.valido = True
        self.dado_de_baja = False

    def __str__(self):
        return "Codigo de casa" + str(self.codigo_casa)+ ", " + "la direccion es " + str(self.direccion)+ ", " + "el numero de dormitorios es "+ str(self.numero_dormitorios)+ ", " + "el numero de cocinas es " + str(self.numero_cocinas) + ", "+ "el numero de comedores es " + str(self.numero_comedores)+ " y el numero de baños es "+str(self.numero_banos)

    def agregar_dormitorio(self, dormitorio):
        self.dormitorios.append(dormitorio)

    def agregar_paquetes_casa(self, paquete_casa):
        self.paquetes_de_casa.append(paquete_casa)

    def dar_de_baja(self):
        """Recibe el objeto Casa y cambia el atributo Dado_de_baja a True"""
        self.dado_de_baja = True


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
        - agregar_paquete_dormitorio
    """

    def __init__(self, casa, numero_camas_sencillas = 0, numero_camas_dobles = 0, tiene_bano_propio = False):
        #La varibale codigo_dormitorio es una variable global
        global codigo_dormitorio
        #Se suma un dígito al codigo_dormitorio para que este sea un código único por instancia
        codigo_dormitorio += 1
        self.codigo_dormitorio = codigo_dormitorio
        #Un dormitorio le pertenece a una única casa
        self.casa = casa
        casa.agregar_dormitorio(self)
        self.numero_camas_dobles = numerocamas_dobles
        self.numero_camas_sencillas = numerocamas_sencillas
        self.tiene_bano_propio = tiene_bano_propio
        #Un dormitorio puede alquilarse por paquetes
        self.paquetes_de_dormitorio = []

    def __str__(self):
        return "codigo_dormitorio" + str(self.codigo_dormitorio)+ ", numerocamas_dobles: " + str(self.numerocamas_dobles) + ", numerocamas_sencillas: " + str(self.numerocamas_sencillas) + ", codigo_casa: " + str(self.casa.codigo_casa)

    def agregar_paquete_dormitorio(self, dormitorio):
        self.paquetes_de_dormitorio.append(dormitorio)

    def reservas(self):
        pass

    def reservas_programadas(self):
        pass

class Paquete:

    """Este objeto representa un paquete de alquiler
        -------------------------------------------
        Atributos:
        - codigo_paquete: integer
        - precio_por_noche: float
        - minimo_de_dias: integer
        - titulo: integer
        -------------------------------------------
        Métodos:
        - Propietario: object
    """

    def __init__(self, tipo, precio_por_noche, numero_de_dias, titulo):
        #La variabel codigo_paquete es global
        global codigo_paquete
        #Se suma una unidad al codigo_paquete para que este código sea único
        codigo_paquete += 1
        self.codigo_paquete = codigo_paquete
        #Los paquetes son de dos tipos: Alquiler de habitación en casa o Alquiler de casa completa
        self.tipo = tipo
        #Es el precio por noche
        self.precio_por_noche = precio_por_noche
        #Es el numero de dias por el que se alquila la habitacion o casa en este paquete
        self.numero_de_dias = numero_de_dias
        #Es el título del anuncio que pone el propietario
        self.titulo = titulo
        #Un paquete puede tener varias reservas
        self.reservas = []

    def __str__(self):
        return "codigo_paquete: " + str(self.codigo_paquete) + ", tipo: "+ str(self.tipo) + ", precio_por_noche: " + str(self.precio_por_noche) + ", descripcion:" + self.descripcion

    def agregar_reserva(self, reserva):
        """Recibe el objeto Paquete y el objeto Reserva. Añade la Reserva al atributo reservas"""
        self.reservas.append(reserva)

class Paquete_de_casa(Paquete):
    """Representa un paquete de alquiler de una casa completa"""
    def __init__(self, casa, precio_por_noche, numero_de_dias, titulo):
        #Un paquete de casa le pertence a una única casa
        self.casa = casa
        super().__init__("Casa completa", precio_por_noche, numero_de_dias, titulo)
        casa.agregar_paquetes_casa(self)

class Paquete_de_dormitorio(Paquete):
    """Representa un paquete de alquiler de un dormitorio en una casa"""
    def __init__(self, dormitorio, precio_por_noche, numero_de_dias, titulo):
        #Un paquete de dormitorio le pertenece a un único dormitorio.
        self.dormitorio = dormitorio
        super().__init__("Habitación", precio_por_noche, numero_de_dias, titulo)
        dormitorio.agregar_paquetes_dormitorio(self)

class Reserva:

    """Este objeto representa la reserva de un paquete de alquiler
        Atributos:
        - codigo_reserva: integer
        - cliente: object
        - paquete: object
        - fecha_de_creacion: datetime
        - fecha_de_inicio_de_reserva: datetime
        - fecha_de_fin_de_reserva: datetime
        - precio: float
        - anulado: boolean
        - pagos: array
        ----------------------------------------------------------
        Métodos:
        - Casa
        - Habitacion
        - numero_de_noches
        """

    def __init__(self, cliente, paquete, fecha_de_creacion, fecha_de_inicio_de_reserva):
        global codigo_reserva
        codigo_reserva += 1
        self.codigo_reserva = codigo_reserva
        self.cliente = cliente
        self.paquete = paquete
        self.fecha_de_inicio_de_reserva = fecha_de_inicio_de_reserva
        self.fecha_de_fin_de_reserva = fecha_de_fin_de_reserva
        self.numero_de_noches = (fecha_de_fin_de_reserva - fecha_de_inicio_de_reserva).days
        self.precio_total = self.numero_de_noches * paquete.precio_por_noche
        self.kcita = kcita
        self.dias = []
        self.estado = "En proceso"
        for i in range(0, self.numero_de_noches + 1):
            self.dias.append(self.fecha_de_inicio_de_reserva + datetime.timedelta(days = i))
        paquete.agregar_reserva(self)
        self.pagos = []

    def __str__(self):
        return "codigo_reserva: " + str(self.codigo_reserva) + ", codigo_paquete:" +str(self.paquete.codigo_paquete) + ", estado: " + self.estado + ", fecha_de_inicio_de_reserva: " + str(self.fecha_de_inicio_de_reserva) + ", fecha_de_fin_de_reserva:" + str(self.fecha_de_fin_de_reserva) + ", numero_de_noches: " + str(self.numero_de_noches) + ", precio_total: " + str(self.precio_total)

    def agregar_pago(self, pago):
        self.pagos.append(pago)

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
        return "cliente:"+str(self.nombre)+"/ celular"+str(self.celular)

class Pago:
    """Representa el pago que hace un cliente a un propietario por la reserva"""
    def __init__(self, reserva, fecha, monto):
        #Un pago corresponde a una única reserva
        self.reserva = reserva
        #Una reserva tiene varios pagos:
        reserva.agregar_pago(self)
        #Un pago se hace en una fecha en específico
        self.fecha = fecha
        #Un pago debe tener un monto específico
        self.monto = monto
        #Se debe verificar que el pago es un número mayor a cero
        while monto < 0:
            monto = float(input("Cantidad inválida, introduzca un número mayor a cero: "))
            self.monto = monto

    def __str__(self):
        pass

class Kcita:

    """Representa la compañia de gestión de reserva de alquileres
        Atributos:
        - Propietarios
        - Clientes
        - Departamentos
    """

    def __init__(self, nombre):
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
        """Recibe Kcita de objeto, usuario de string y password de string. Si el usuario y password es correcto, inicia una sesión."""
        if not self.sesion_iniciada:
            for propietario in self.propietarios:
                if propietario.usuario == usuario and propietario.password == password:
                    propietario.sesion_iniciada = True
                    self.sesion_iniciada = True
            if not self.sesion_iniciada:
                print("Nombre de usuario y contraseña no coinciden.")
        else:
            print("Ya tiene una sesión abierta")

    def salir_sesion(self, propietario):
        self.sesion_iniciada = False
        propietario.sesion_iniciada = False

    def busqueda(self, codigo_casa, dia_de_entrada, numero_de_noches):
        """Recibe un código de casa (int), un dia de entrada (datetime.date) y un numero de noches (int).
            Devuleve una array de paquetes o un mensaje de error (str)"""

        busqueda_valida = False

        for casa in self.casas:
            #El código de la Casa es único y debe coincidir. Además, la Casa no debe haber sido dado de baja por el Propietario.
            if casa.codigo_casa == codigo_casa and not casa.dado_de_baja:
                #Hay una única casa a la cual le corresponde el código
                casaRef = casa
                #Si se encuentra una casa, la busqueda es válida
                busqueda_valida += True
                break

        if not busqueda_valida:
            return "Código de casa no encontrado"
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

        if len(paquetes_disponibles) == 0:
            return "No se encontraron paquetes disponibles con esa fecha. Intente cambiando de fecha o número de noches"
        else:
            return paquetes_disponibles


def test():

    #Creación de objecto Kcita
    kcita = Kcita("Kcita")

    #Creación de departamentos
    departamento = Departamento(kcita, "Lima")
    departamento2 = Departamento(kcita, "Arequipa")
    departamento3 = Departamento(kcita, "Cuzco")

    #Creación de clientes
    cliente1 = Cliente(kcita, "Renato Palomino", "938618324", "r.palomino@gmail.com")
    cliente2 = Cliente(kcita, "Sebastian Ramos", "978762123", "s.ramos@gmail.com")
    cliente3 = Cliente(kcita, "Estefania Ortega", "938711189", "e.ortega@hotmail.com")

    #Creación de propietarios
    propietario1 = Propietario(kcita, "paolobejarano", "12345", "Paolo Bejarano")
    propietario2 = Propietario(kcita, "carrrdenas", "bea", "Alvaro Cardenas")

    #El siguiente propietario tiene un nombre de usuario invalido pues se repite
    propietario3 = Propietario(kcita, "PaoloBejaranO", "31982", "Paolo Bejarano")

    #Creación de casas y dormitorios
    casa1 = Casa(propietario1, departamento, "Av. Parque Las leyendas, San Miguel", 1, 1, 1, 1, 1)
    dormitorio11 = Dormitorio(casa2, 1, 2)
    dormitorio12 = Dormitorio(casa2, 1, 2)
    dormitorio13 = Dormitorio(casa2, 1, 2)
    casa2 = Casa(propietario1, departamento, "Av. Reducto, Miraflores", 2, 1, 1, 1)
    dormitorio21 = Dormitorio(casa2, 1, 2)
    dormitorio22 = Dormitorio(casa2, 1, 2)
    dormitorio23 = Dormitorio(casa2, 1, 2)
    casa3 = Casa(propietario2, departamento, "Av. Salaverry, Jesus MAria", 2, 1, 1, 1)
    dormitorio31 = Dormitorio(casa2, 1, 2)
    dormitorio32 = Dormitorio(casa2, 1, 2)
    dormitorio32 = Dormitorio(casa2, 1, 2)


    #Creación de dormitorios

    dormitorio = Dormitorio(casa2, 1, 2)
    paquete1 = Paquete_de_casa(casa, 30.0, "Casa en alquiler")
    paquete2 = Paquete_de_dormitorio(dormitorio, 15.0, "Departamento en alquiler")
    reserva1 = Reserva(cliente1, paquete1, datetime.date(2019, 6, 21), datetime.date(2019, 6, 24))
    reserva2 = Reserva(cliente2, paquete2, datetime.date(2019, 6, 22), datetime.date(2019, 6, 25))

    #Test de métodos str
    print(paquete1)
    print(paquete1.casa)
    print(paquete2)
    print(paquete2.dormitorio)

    print(reserva1)
    print("--------------")
    print(reserva1.dias)
    print(reserva1.paquete)
    print(paquete1.reservas)
    print(reserva2)

    #Test de atributos de objeto Kcita
    print(kcita.departamentos)
    print(kcita.clientes)
    print(kcita.propietarios)

    print(casa.paquetes_de_casa)
    print(dormitorio.paquetes_de_dormitorio)

    print(departamento.casas)

    print(departamento.paquetes())

    #Búsqueda válida
    print(kcita.busqueda(1, datetime.date(2019, 6, 30), 2))
    #Búsqueda inválida debido a la fecha
    print(kcita.busqueda(1, datetime.date(2019, 6, 21), 2))
    #Búsqueda inválida debido al código de la casa
    print(kcita.busqueda(10, datetime.date(2019, 6, 30), 2))

    print(kcita.propietario_signed_in("usuario1", "12345"))
    print(kcita.propietario_signed_in("usuario3", "12345"))
    print(kcita.propietario_signed_in("usuario1", "345"))

test()

def interfaz():
    gui = Tk()
    gui.geometry("1250x750")
    gui.title("Kcita: Alquileres de casas y dormitorios")
    ttk.Button(gui, text="Iniciar sesión").grid()
    ttk.Button(gui, text="Resgistrarme").grid()
    gui.mainloop()

#interfaz()
