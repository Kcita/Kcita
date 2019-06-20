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

from tqdm import tqdm
from pyfiglet import figlet_format
import time

def CLI():

    kcita = Kcita("Kcita")

    #Creacion de departamentos
    departamento = Departamento(kcita, "Lima")
    departamento2 = Departamento(kcita, "Arequipa")

    while True:
        print(figlet_format(kcita.nombre))
        print("Bienvenido a Kcita. Desde aquí podrás alquilar un inmueble o poner en alquiler tu inmueble.")
        print("Presiona Ctrl + C para salir en cualquier momento.")
        opcion = int(input("Escribe (1) si deseas alquilar un inmueble o (2) si deseas poner tu inmueble en alquiler\n"))
        while not(opcion == 1 or opcion == 2):
            opcion = int(input("Opción incorrecta. Escribe (1) si deseas alquilar un inmueble o (2) si deseas poner tu inmueble en alquiler\n"))
        if opcion == 1:
            for i in tqdm(range(100)):
                time.sleep(1)
        break

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
    dormitorio11 = Dormitorio(casa1, 1, 2)
    dormitorio12 = Dormitorio(casa1, 1, 2)
    dormitorio13 = Dormitorio(casa1, 1, 2)
    casa2 = Casa(propietario1, departamento, "Av. Reducto, Miraflores", 2, 1, 1, 1)
    dormitorio21 = Dormitorio(casa2, 1, 2)
    dormitorio22 = Dormitorio(casa2, 1, 2)
    dormitorio23 = Dormitorio(casa2, 1, 2)
    casa3 = Casa(propietario2, departamento, "Av. Salaverry, Jesus MAria", 2, 1, 1, 1)
    dormitorio31 = Dormitorio(casa3, 1, 2)
    dormitorio32 = Dormitorio(casa3, 1, 2)
    dormitorio32 = Dormitorio(casa3, 1, 2)


    #Creación de paquetes
    paquete1 = PaqueteCasa(casa1, 30.0, 3, "Casa en alquiler")
    paquete2 = PaqueteDormitorio(dormitorio21, 15.0, 4, "Departamento en alquiler")
    reserva1 = Reserva(cliente1, paquete1, datetime.date(2019, 6, 19), datetime.date(2019, 6, 21))
    reserva2 = Reserva(cliente2, paquete2, datetime.date(2019, 6, 18), datetime.date(2019, 6, 22))

    #Test de métodos str
    print(paquete1)
    print(paquete1.casa)
    print(paquete2)
    print(paquete2.dormitorio)

    print(reserva1)
    print(reserva1.dias)
    print(reserva1.paquete)
    print(paquete1.reservas)
    print(reserva2)

    #Test de atributos de objeto Kcita
    print(kcita.departamentos)
    print(kcita.clientes)
    print(kcita.propietarios)

    print(casa1.paquetes_de_casa)
    print(dormitorio21.paquetes_de_dormitorio)

    print(departamento.casas)

    print(departamento.paquetes())

    #Búsqueda válida
    print(kcita.busqueda(1, datetime.date(2019, 6, 30), 2))
    #Búsqueda inválida debido a la fecha
    print(kcita.busqueda(1, datetime.date(2019, 6, 21), 2))
    #Búsqueda inválida debido al código de la casa
    print(kcita.busqueda(10, datetime.date(2019, 6, 30), 2))

    print(reserva1.precio_total)
    pago1 = Pago(reserva1, 20.5)
    pago2 = Pago(reserva1, 20)
    print(reserva1.monto_cobrado())

    #print(kcita.propietario_signed_in("usuario1", "12345"))
    #print(kcita.propietario_signed_in("usuario3", "12345"))
    #print(kcita.propietario_signed_in("usuario1", "345"))

CLI()
