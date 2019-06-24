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


def inicio_sesion():
    pass

def registrarse():
    pass

def menu_cuenta():
    pass

def menu_casas():
    pass

def menu_paquetes():
    pass

def menu_reservas():
    pass

def menu_principal_cliente():
    pass

def menu_principal_propietario():
    pass

def CLI():

    kcita = Kcita("Kcita")

    #Creacion de departamentos
    departamento = Departamento(kcita, "Lima")
    departamento2 = Departamento(kcita, "Arequipa")

    while True:
        print("Bienvenido a Kcita. Desde aquí podrás alquilar un inmueble o poner en alquiler tu inmueble.")
        print("Presiona Ctrl + C para salir en cualquier momento.")
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
                numero_dormitorios = input("Introduzca el número de dormitorios: ")
                numero_banos = input("Introduzca el número de baños: ")
                numero_cocinas = input("Introduzca el número de cocinas: ")
                numero_comedores = input("Introduzca el número de comedores: ")
                numero_plazas_garaje = input("Introduzca el número de plazas de garaje: ")
                descripcion_general = input("Introduzca una descripción: ")
                nueva_casa = Casa(propietario, departamento, direccion, numero_dormitorios, numero_banos, numero_cocinas, numero_comedores, numero_plazas_garaje, descripcion_general)
                for i in range(0, numero_dormitorios):
                    print("Para su " + i + "º dormitorio, indique lo siguiente: ")
                    numero_camas_sencillas = int(input("¿Cuántas camas sencillas tiene? "))
                    numero_camas_dobles = int(input("¿Cuántas camas dobles tiene? "))
                    tiene_bano_propio = input("¿Tiene baño propio? (V/F)")
                    if tiene_bano_propio == "V":
                        tiene_bano_propio = True
                    elif tiene_bano_propio == "F":
                        tiene_bano_propio = False
                    nuevo_dormitorio = Dormitorio(casa, numero_camas_sencillas, numero_camas_dobles, tiene_bano_propio)





CLI()
