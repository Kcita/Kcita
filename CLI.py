from src.departamento import Departamento
from src.casa import Casa
from src.kcita import Kcita
from src.paquete import PaqueteCasa
from src.paquete import PaqueteDormitorio
from src.propietario import Propietario
from src.cliente import Cliente
from src.dormitorio import Dormitorio
from src.reserva import Reserva
from src.pago import Pago

import datetime

kcita = Kcita("Kcita")
departamento1 = Departamento(kcita, "Lima")
departamento2 = Departamento(kcita, "Arequipa")

def valor_logico(cadena):
    """Recibe una cadena de texto. Asume que esta es V o F. Devuelve el valor lógico"""
    if cadena == "V":
        return True
    elif cadena == "F":
        return False

def CLI():

    kcita = Kcita("Kcita")

    #Creacion de departamentos
    departamento = Departamento(kcita, "Lima")
    departamento2 = Departamento(kcita, "Arequipa")

    print("Bienvenido a Kcita. Desde aquí podrás alquilar un inmueble o poner en alquiler tu inmueble.")
    print("Presiona Ctrl + C para salir en cualquier momento.")

    while True:
        opcion = int(input("Escribe (1) si deseas alquilar un inmueble o (2) si deseas poner tu inmueble en alquiler\n"))
        while not(opcion == 1 or opcion == 2):
            opcion = int(input("Opción incorrecta. Escribe (1) si deseas alquilar un inmueble o (2) si deseas poner tu inmueble en alquiler\n"))
        if opcion == 1:
            pass
        elif opcion == 2:
            print("Para ver su cuentas (1)")
            print("Para ver sus casas introduzca (2)")
            print("Para ver sus paquetes introduzca (3)")
            print("Para ver sus reservas introduzca (4)")
            print("Para ver los pagos introduzca (5)")
            opcion = int(input("Opcion: "))
            while not(opcion == 1 or opcion == 2 or opcion == 3 or opcion == 4 or opcion == 5):
                opcion = int(input("Opción incorrecta. Intente nuevamente."))

        if opcion == 1:
            print("Para iniciar sesión introduzca (1)")
            print("Para registrarse introduzca (2)")
            print("Para cerrar sesión introduzca (3)")
            opcion = int(input("Opcion: "))
            while not(opcion == 1 or opcion == 2 or opcion == 3):
                opcion = int(input("Opción incorrecta. Intente nuevamente."))
            if opcion == 1:
                usuario_a_verificar = input("Ingrese su usuario: ")
                password_a_verificar = input("Ingrese su contraseña: ")
                kcita.iniciar_sesion(usuario_a_verificar, password_a_verificar)
            elif opcion == 2:
                usuario_nuevo = input("Ingrese su usuario: ")
                password_nuevo = input("Ingrese su contraseña: ")
                nombre_nuevo = input("Ingrese su nombre: ")
                nuevo_propietario = Propietario(kcita, usuario_nuevo, password_nuevo, nombre_nuevo)
                nuevo_propietario.sesion_iniciada
            elif opcion == 3:
                kcita.salir_sesion()
        elif opcion == 2:
            print("Para agregar una nueva casa introduzca (1)")
            print("Para ver sus casas introduzca (2)")
            print("Para editar una de sus casas introduzca (3)")
            print("Para dar de baja a una de sus casas introduzca (4)")
            opcion = int(input("Opcion: "))
            if opcion == 1:
                print("----------")
                print("Departamentos disponibles: ")
                for departamento in kcita.departamentos:
                    print("-", departamento.codigo_departamento, ": ", departamento.nombre)
                codigo_departamento = int(input("Introduzca el código del departamento: "))
                departamento = kcita.busqueda_de_departamento_por_codigo(codigo_departamento)
                direccion = input("Introduzca su dirección: ")
                numero_dormitorios = int(input("Introduzca el número de dormitorios: "))
                numero_banos = int(input("Introduzca el número de baños: "))
                numero_cocinas = int(input("Introduzca el número de cocinas: "))
                numero_comedores = int(input("Introduzca el número de comedores: "))
                numero_plazas_garaje = int(input("Introduzca el número de plazas de garaje: "))
                descripcion_general = input("Introduzca una descripción: ")
                propietario_logeado = Kcita.propietario_logeado()
                nueva_casa = Casa(propietario_logeado, departamento, direccion, numero_dormitorios, numero_banos, numero_cocinas, numero_comedores, numero_plazas_garaje, descripcion_general)
                for i in range(0, numero_dormitorios):
                    print("Para su " + i + "º dormitorio, indique lo siguiente: ")
                    numero_camas_sencillas = int(input("¿Cuántas camas sencillas tiene? "))
                    numero_camas_dobles = int(input("¿Cuántas camas dobles tiene? "))
                    tiene_bano_propio = input("¿Tiene baño propio? (V/F)")
                    tiene_bano_propio = valor_logico(tiene_bano_propio)
                    nuevo_dormitorio = Dormitorio(nueva_casa, numero_camas_sencillas, numero_camas_dobles, tiene_bano_propio)
                for i in range(0, numero_cocinas):
                    print("Para su " + i + "º cocina, indique lo siguiente: ")
                    tiene_lavavajillas = input("¿Tiene lavavajillas? (V/F)")
                    tiene_lavavajillas = valor_logico(tiene_lavavajillas)
                    tiene_lavadoras = input("¿Tiene lavadoras? (V/F)")
                    tiene_lavadoras = valor_logico(tiene_lavadoras)
                    nueva_cocina = Cocina(nueva_casa, tiene_lavavajillas, tiene_lavadoras)
            elif opcion == 2:
                for casa in propietario_logeado.casas:
                    print(casa)

CLI()


def cli2():
    print("Opciones de busquedas:")
    kcita=Kcita("kcita")
    departamento = Departamento(kcita, "Lima")
    departamento2 = Departamento(kcita, "Arequipa")
    cliente1 = Cliente(kcita, "Renato Palomino", "938618324", "r.palomino@gmail.com")
    cliente2 = Cliente(kcita, "Sebastian Ramos", "978762123", "s.ramos@gmail.com")
    propietario1 = Propietario(kcita, "paolobejarano", "12345", "Paolo Bejarano")
    propietario2 = Propietario(kcita, "carrrdenas", "bea", "Alvaro Cardenas")
    casa1 = Casa(propietario1, departamento, "Av. Parque Las leyendas, San Miguel", 1, 1, 1, 1, 1)
    dormitorio11 = Dormitorio(casa1, 1, 2)
    dormitorio12 = Dormitorio(casa1, 1, 2)
    dormitorio13 = Dormitorio(casa1, 1, 2)
    casa2 = Casa(propietario1, departamento, "Av. Reducto, Miraflores", 2, 1, 1, 1)
    dormitorio21 = Dormitorio(casa2, 1, 2)
    dormitorio22 = Dormitorio(casa2, 1, 2)

    paquete1 = PaqueteCasa(casa1, 30.0, 3, "Casa en alquiler")
    paquete2 = PaqueteDormitorio(dormitorio21, 15.0, 4, "Departamento en alquiler")


    print("Busqueda por codigo de casa, fecha de entrada y numero de noches (1)")
    print("Busqueda por atributos y valores (2)")
    opcion=int(input("Opcion: "))
    if opcion==1:
        print("eligió la busqeuda numero 1")
        codigo_casa=input("Ingrese el codigo de casa: ")
        año=int(input("ingres el año: "))
        mes=int(input("ingrese el mes: "))
        dia=int(input("ingrese el día: "))
        fecha=datetime.date(año,mes,dia)
        numero_noches=int(input("Ingrese el numero de noches: "))
        kcita.busqueda(codigo_casa,fecha,numero_noches)
    elif opcion==2:
        print("Eligió la busqueda numero 2")
        print("Puede elegir entre estos atributos: ")
        print("(1) Número de baños")
        print("(2) Número de cocinas")
        print("(3) Número de dormitorios")
