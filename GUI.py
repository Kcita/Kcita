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
from tkinter import *
from tkinter import ttk
import time

global main_screen


#Datos iniciales
kcita = Kcita("Kcita")
departamento1 = Departamento(kcita, "Lima")
departamento2 = Departamento(kcita, "Arequipa")
cliente1 = Cliente(kcita, "Renato Palomino", "938618324", "r.palomino@gmail.com")
cliente2 = Cliente(kcita, "Sebastian Ramos", "978762123", "s.ramos@gmail.com")
cliente3 = Cliente(kcita, "Estefania Ortega", "938711189", "e.ortega@hotmail.com")
cliente4= Cliente(kcita,"Lucio Lazarte","986764554","lucio45@gmail.com")
propietario1 = Propietario(kcita, "renato", "1234", "Renato Palomino")
propietario2 = Propietario(kcita, "paolo", "1234", "Paolo Bejarano")
casa1 = Casa(propietario1, departamento1, "Av. Salaverry 2020, Jesus María", 3, 2, 2, 1, 1)
dormitorio11 = Dormitorio(casa1, 1, 2)
dormitorio12 = Dormitorio(casa1, 1, 2)
dormitorio13 = Dormitorio(casa1, 1, 2)
casa2 = Casa(propietario1, departamento1, "Av. Reducto 701, Miraflores", 3, 3, 1, 1)
dormitorio21 = Dormitorio(casa2, 1, 2)
dormitorio22 = Dormitorio(casa2, 1, 2)
dormitorio23 = Dormitorio(casa2, 1, 2)
casa3 = Casa(propietario2, departamento1, "Av. Javier Prado 315, San Isidro", 4, 3, 1, 1)
dormitorio31 = Dormitorio(casa3, 1, 2)
dormitorio32 = Dormitorio(casa3, 1, 2)
dormitorio33 = Dormitorio(casa3, 1, 2)

    #PAQUETES CASA
paqueteporcasa=PaqueteCasa(casa1, 300, 4, "se alquila casa a 300 soles la nocheminimo de noches 4" )
paqueteporcasa1=PaqueteCasa(casa2, 400,3,"se alcuila casa a 350 soles, minimo de noches 3")
paqueteporcasa2=PaqueteCasa(casa3, 280,3,"se alquila casa a 300 soles, minimo de noches 3")

    #PAQUETES dormitorio
paquetepordormitorio=PaqueteDormitorio(dormitorio11,50, 2,"se alquila dormitorio a 50 soles la noche, minimo de noches 2")
paquetepordormitorio1=PaqueteDormitorio(dormitorio12, 60,2,"se alquila dormitorio a 60 soles la noche, minimo de noches 2")

paquetepordormitorio3=PaqueteDormitorio(dormitorio21,100,2,"se alquila dormitorio a 100 soles la noche,minimo de noches 2")

    #reservas
reserva1=Reserva(cliente1,paqueteporcasa,datetime.date(2019,3,24),datetime.date(2019,3,30),datetime.date(2019,4,4))
reserva2=Reserva(cliente2,paqueteporcasa1,datetime.date(2019,4,15),datetime.date(2019,4,30),datetime.date(2019,5,5))
reserva3=Reserva(cliente3,paqueteporcasa,datetime.date(2019,3,24),datetime.date(2019,3,30),datetime.date(2019,4,4))
reserva4=Reserva(cliente4,paquetepordormitorio,datetime.date(2019,5,1),datetime.date(2019,5,5),datetime.date(2019,5,9))
reserva5=Reserva(cliente1,paquetepordormitorio3,datetime.date(2019,6,14),datetime.date(2019,6,20),datetime.date(2019,6,25))

def sign_in_verify():
    usuario = usuario_verify.get()
    password = password_verify.get()
    print("hola")
    success = kcita.iniciar_sesion(usuario, password)
    if success:
        Label(sign_in_screen, text="Inicio de sesión satisfactorio").pack()
        global propietario
        propietario = kcita.propietario_logeado()
        time.sleep(2)
        sign_in_screen.destroy()
    else:
        Label(sign_in_screen, text="Usuario y contraseña no coinciden").pack()

def sign_in_screen():
    global sign_in_screen
    sign_in_screen = Tk()
    sign_in_screen.title("Iniciar sesión")
    sign_in_screen.geometry("300x250")

    #Variables
    global usuario_verify
    global password_verify
    usuario_verify = StringVar()
    password_verify = StringVar()

    #Nombre de usuario
    username_label = Label(sign_in_screen, text="Nombre de usuario").pack()
    username_entry = Entry(sign_in_screen, textvariable=usuario_verify).pack()

    #Contraseña
    password_label = Label(sign_in_screen, text="Contraseña").pack()
    password_entry = Entry(sign_in_screen, textvariable=password_verify, show='*').pack()

    #Botón
    Button(sign_in_screen, text="Iniciar sesión", width=10, height=1, command = sign_in_verify).pack()

def registrarse():

    nombre = nombre_new.get()
    usuario = usuario_new.get()
    password = password_new.get()

    nuevo_propietario = Propietario(kcita, usuario, password, nombre)
    time.sleep(2)
    sign_up_screen.destroy()

def cerrar_sesion():
    kcita.salir_sesion()
    global propietario
    propietario = None

def sign_up_screen():
    global sign_up_screen
    sign_up_screen = Tk()
    sign_up_screen.title("Iniciar sesión")
    sign_up_screen.geometry("300x250")

    #Variables
    global nombre_new
    global usuario_new
    global password_new
    nombre_new = StringVar()
    usuario_new = StringVar()
    password_new = StringVar()

    #Nombre de usuario
    username_label = Label(sign_up_screen, text="Nombre de usuario").pack()
    username_entry = Entry(sign_up_screen, textvariable=usuario_new).pack()

    #Contraseña
    password_label = Label(sign_up_screen, text="Contraseña").pack()
    password_entry = Entry(sign_up_screen, textvariable=password_new, show='*').pack()

    #Nombre
    nombre_label = Label(sign_up_screen, text="Nombre completo").pack()
    nombre_entry = Entry(sign_up_screen, textvariable=nombre_new).pack()

    #Botón
    Button(sign_up_screen, text="Registrarse", width=10, height=1, command = registrarse).pack()

def codigos_departamentos_disponibles():
    departamentos_screen = Tk()
    departamentos_screen.title("Departamentos disponibles")

    for departamento in kcita.departamentos:
        codigo_mas_departamento = str(departamento.codigo_departamento) + ": " + departamento.nombre
        Label(departamentos_screen, text=codigo_mas_departamento).pack()

def casa_create():

    """Esta funcion se activa al darle click al boton Agregar Casas
        Lee los datos ingresados por el usuario para crear una nueva casa."""

    codigo_departamento = codigo_departamento_entry.get()
    departamento = kcita.busqueda_de_departamento_por_codigo(int(codigo_departamento))
    direccion = direccion_entry.get()
    numero_dormitorios = int(numero_dormitorios_entry.get())
    numero_cocinas = int(numero_cocinas_entry.get())
    numero_banos = int(numero_banos_entry.get())
    numero_plazas_garaje = int(numero_plazas_garaje_entry.get())
    descripcion_general = descripcion_general_entry.get()
    nueva_casa = Casa(propietario, departamento, direccion, numero_dormitorios, numero_cocinas, numero_banos, numero_plazas_garaje, descripcion_general)

    time.sleep(2)
    casa_new_screen.destroy()

def casa_new():

    """Esta función produce un formulario para agregar una nueva casa"""
    global casa_new_screen
    casa_new_screen = Tk()
    casa_new_screen.geometry("500x700")
    casa_new_screen.title("Agregar una nueva casa")

    #Variables

    #Codigo_departamento
    codigo_departamento_label = Label(casa_new_screen, text="Código de departamento").pack()
    global codigo_departamento_entry
    codigo_departamento_entry = Entry(casa_new_screen, textvariable="codigo_departamento_casa_new")
    codigo_departamento_entry.pack()
    Button(casa_new_screen, text= "Ver departamentos disponibles", height=1, width=20, command=codigos_departamentos_disponibles).pack()

    #direccion
    var1 = Label(casa_new_screen, text="Dirección").pack()
    global direccion_entry
    direccion_entry = Entry(casa_new_screen, textvariable="direccion_casa_new")
    direccion_entry.pack()

    #numero de dormitorios
    var3 = Label(casa_new_screen, text="¿Cuántos dormitorios tienes?").pack()
    global numero_dormitorios_entry
    numero_dormitorios_entry = Entry(casa_new_screen, textvariable="numero_dormitorios_casa_new")
    numero_dormitorios_entry.pack()

    #numero de cocinas
    var5 = Label(casa_new_screen, text="¿Cuántos baños tiene?").pack()
    global numero_banos_entry
    numero_banos_entry = Entry(casa_new_screen, textvariable="numero_banos_casa_new")
    numero_banos_entry.pack()

    #Numero de baños
    var7 = Label(casa_new_screen, text="¿Cuántas cocinas tiene?").pack()
    global numero_cocinas_entry
    numero_cocinas_entry = Entry(casa_new_screen, textvariable="numero_cocinas_casa_new")
    numero_cocinas_entry.pack()

    #Número de plazas de garaje
    var9 = Label(casa_new_screen, text="¿Cuántas plazas de garaje tiene?").pack()
    global numero_plazas_garaje_entry
    numero_plazas_garaje_entry = Entry(casa_new_screen, textvariable="numero_plazas_garaje_casa_new")
    numero_plazas_garaje_entry.pack()

    #Descripción general
    var11 = Label(casa_new_screen, text="Escribe una breve descripción sobre la casa").pack()
    global descripcion_general_entry
    descripcion_general_entry = Entry(casa_new_screen, textvariable="descripcion_general_casa_new")
    descripcion_general_entry.pack()

    boton = Button(casa_new_screen, text="Añadir", height=1, width=20, command = casa_create)
    boton.pack()

def casa_index():

    """Muestra todas las casas que ha puesto el usuario"""
    casa_index_screen = Tk()
    casa_index_screen.title("Ver mis casas")
    if len(propietario.casas) == 0:
        Label(casa_index_screen, text="No ha agregado ninguna casa hasta el momento.").pack()
    elif len(propietario.casas) >= 1:
        Label(casa_index_screen, text="ID").grid(row=0, column=0)
        Label(casa_index_screen, text="Departamento").grid(row=0, column=1)
        Label(casa_index_screen, text="Direccion").grid(row=0, column=2)
        Label(casa_index_screen, text="Dormitorios").grid(row=0, column=3)
        Label(casa_index_screen, text="Baños").grid(row=0, column=4)
        Label(casa_index_screen, text="Cocinas").grid(row=0, column=5)
        Label(casa_index_screen, text="Comedores").grid(row=0, column=6)
        Label(casa_index_screen, text="Garajes").grid(row=0, column=7)
        j = 1
        for casa in propietario.casas:
            if not casa.dado_de_baja:
                Label(casa_index_screen, text=str(casa.codigo_casa)).grid(row=j, column=0)
                Label(casa_index_screen, text=casa.departamento.nombre).grid(row=j, column=1)
                Label(casa_index_screen, text=casa.direccion).grid(row=j, column=2)
                Label(casa_index_screen, text=casa.numero_dormitorios).grid(row=j, column=3)
                Label(casa_index_screen, text=casa.numero_banos).grid(row=j, column=4)
                Label(casa_index_screen, text=casa.numero_cocinas).grid(row=j, column=5)
                Label(casa_index_screen, text=casa.numero_comedores).grid(row=j, column=6)
                Label(casa_index_screen, text=casa.numero_plazas_garaje).grid(row=j, column=7)
                j += 1
    else:
        Label(casa_index_screen, text="Tiene que iniciar sesión para poder ver sus casas.").pack()

def casa_edit():

    """Muestra un formulario para editar una casa"""

    casa_edit_screen = Tk()
    casa_edit_screen.title("Editar casa")


def casa_update():
    pass

def casa_destroy():
    pass

def casa_delete():
    """Presenta un formulario para borrar una casa"""
    global casa_delete_screen
    casa_delete_screen = Tk()
    casa_delete_screen.title("Dar de baja una casa")

    global casa_delete_entry
    Label(casa_delete_screen, text="Introduzca el codigo de la casa que desea dar de baja.")
    #Button()

def reserva_create():
    pass

def reserva_new():

    global reserva_new_screen
    reserva_new_screen = Tk()
    reserva_new_screen.title("Nueva reserva")

    Label(reserva_new_screen, text="Introduzca el código del paquete").pack()
    codigo_paquete_entry = Entry()
    codigo_paquete_entry.pack()
    Label(reserva_new_screen, text="Introduzca la fecha de inicio").pack()
    fecha_de_inicio_de_reserva = Entry()
    fecha_de_inicio_de_reserva.pack()
    fecha_de_fin_de_reserva = Entry()
    fecha_de_fin_de_reserva.pack()


def reserva_destroy():
    reserva = int(codigo_reserva_entry.get())

def reserva_delete():
    global reserva_delete_screen
    reserva_delete_screen = Tk()
    reserva_delete_screen.title("Anular reserva")

    Label(reserva_delete_screen, text="Introduzca el código de la reserva que desea añadir:")
    global codigo_reserva_entry
    codigo_reserva_entry = Entry(reserva_delete_screen, text="")
    Button(codigo_reserva_entry, text= "Anular", height=2, width=25, command=busqueda1_result).pack()


def reserva_index_propietario():

    global reserva_index_propietario
    reserva_index_propietario = Tk()
    reserva_index_propietario.title("Mis reservas")

    if len(propietario.reservas()) == 0:
        Label(reserva_index_propietario, text="Todavía nadie ha hecho una reserva").pack()
    else:
        Label(reserva_index_propietario, text="ID").grid(row=0, column=0)
        Label(reserva_index_propietario, text="ID de paquete").grid(row=0, column=1)
        Label(reserva_index_propietario, text="Fecha de creacion").grid(row=0, column=2)
        Label(reserva_index_propietario, text="Fecha de inicio de reserva").grid(row=0, column=3)
        Label(reserva_index_propietario, text="Fecha de fin de reserva").grid(row=0, column=4)
        Label(reserva_index_propietario, text="Estado").grid(row=0, column=5)
        Label(reserva_index_propietario, text="Nombre cliente").grid(row=0, column=6)
        Label(reserva_index_propietario, text="Celular cliente").grid(row=0, column=7)
        i = 1
        for reserva in propietario.reservas:
            Label(reserva_index_propietario, text=reserva.codigo_reserva).grid(row=i, column=0)
            Label(reserva_index_propietario, text=reserva.paquete.codigo_paquete).grid(row=i, column=1)
            Label(reserva_index_propietario, text=reserva.fecha_de_creacion).grid(row=i, column=2)
            Label(reserva_index_propietario, text=reserva.fecha_de_inicio_de_reserva).grid(row=i, column=3)
            Label(reserva_index_propietario, text=reserva.fecha_de_fin_de_reserva).grid(row=i, column=4)
            observacion = ""
            if reserva.anulado:
                observacion = "Anulado"
            elif reserva.adelanto_esta_atrasado():
                observacion = "Está atrasado"
            Label(reserva_index_propietario, text=observacion).grid(row=i, column=5)
            Label(reserva_index_propietario, text=reserva.cliente.nombre).grid(row=i, column=6)
            Label(reserva_index_propietario, text=reserva.cliente.celular).grid(row=i, column=7)
            i = i + 1

def reserva_index_cliente():

    reserva_index_cliente_screen = Tk()
    reserva_index_cliente_screen.title("Mis reservas")



    #for reserva in cliente.reservas


def pago_create():
    pass

def pago_new():
    pago_new_screen = Tk()
    pago_new_screen.title("Nuevo pago")

def busqueda1_result():

    busqueda1_result_screen = Tk()
    busqueda1_result_screen.title("Resultado de búsqueda")

    codigo_departamento = int(codigo_departamento_entry.get())

    departamento = kcita.busqueda_de_departamento_por_codigo(codigo_departamento)

    if len(departamento.paquetes_disponibles()) == 0:
        Label(busqueda1_result_screen, text="No se ha encontrado ningún alquiler.").pack()
    else:
        Label(busqueda1_result_screen, text="Codigo").grid(row=0, column=0)
        Label(busqueda1_result_screen, text="Tipo").grid(row=0, column=1)
        Label(busqueda1_result_screen, text="Precio/dia").grid(row=0, column=2)
        Label(busqueda1_result_screen, text="Numero de dias").grid(row=0, column=3)
        Label(busqueda1_result_screen, text="Ubicacion").grid(row=0, column=4)
        i = 1
        for paquete in departamento.paquetes_de_casa_disponibles():
            Label(busqueda1_result_screen, text=paquete.codigo_paquete).grid(row=i, column=0)
            Label(busqueda1_result_screen, text=paquete.tipo).grid(row=i, column=1)
            Label(busqueda1_result_screen, text=paquete.precio_por_dia).grid(row=i, column=2)
            Label(busqueda1_result_screen, text=paquete.numero_de_dias).grid(row=i, column=3)
            Label(busqueda1_result_screen, text=paquete.casa.direccion).grid(row=i, column=4)
            i += 1
        i = 1
        for paquete in departamento.paquetes_de_dormitorio_disponibles():
            Label(busqueda1_result_screen, text=paquete.codigo_paquete).grid(row=i, column=0)
            Label(busqueda1_result_screen, text=paquete.tipo).grid(row=i, column=1)
            Label(busqueda1_result_screen, text=paquete.precio_por_dia).grid(row=i, column=2)
            Label(busqueda1_result_screen, text=paquete.numero_de_dias).grid(row=i, column=3)
            Label(busqueda1_result_screen, text=paquete.dormitorio.casa.direccion).grid(row=i, column=4)
            i += 1


def busqueda1_form():
    busqueda1_form_screen = Tk()
    busqueda1_form_screen.title("Búsqueda por departamento")

    global codigo_departamento_entry

    codigo_departamento_entry = Entry(busqueda1_form_screen, textvariable="codigo_departamento")
    codigo_departamento_entry.pack()
    Button(busqueda1_form_screen, text= "Ver departamentos disponibles", height=1, width=25, command=codigos_departamentos_disponibles).pack()
    Button(busqueda1_form_screen, text= "Buscar", height=2, width=25, command=busqueda1_result).pack()


def main_screen():
    main_screen = Tk()
    main_screen.geometry("1200x700")
    main_screen.title("Kcita: reserva de dormitorios y casas")

    titulo_cliente = Label(main_screen, text = "Cliente",height=1, width=15 , font=("Open Sans", 35, "bold"))
    titulo_cliente.place(x=150, y=10)

    Label(main_screen, text = "Búsqueda de alquileres",height=1, font=("Open Sans", 35)).place(x=25, y=100)

    Button(main_screen, text = "Búsqueda por departamento", height=2, width=25, command = busqueda1_form).place(x=200, y=150)

    #Button(main_screen, text = "Búsqueda 2", height=2, width=25).place(x=200, y=150)

    #Button(main_screen, text = "Búsqueda 3", height=2, width=25).place(x=200, y=150)

    titulo_propietario = Label(main_screen, text = "Propietario",height=1, width=15 , font=("Open Sans", 35 , "bold"))
    titulo_propietario.place(x=750, y=10)

    #Boton de logeo de propietario
    sign_in = Button(main_screen, text = "Iniciar sesión", height=1, width=15, command=sign_in_screen)
    sign_in.place(x=700, y=75)

    sign_up = Button(main_screen, text = "Registrarse", height=1, width=15, command=sign_up_screen)
    sign_up.place(x=850, y=75)

    log_out = Button(main_screen, text = "Cerrar sesión", height=1, width=15, command=cerrar_sesion)
    log_out.place(x=1000, y=75)

    Label(main_screen, text = "Casas",height=1, font=("Open Sans", 35)).place(x=675, y=100)

    Button(main_screen, text = "Agregar casa", height=1, width=15, command = casa_new).place(x=800, y=150)
    Button(main_screen, text = "Ver casas", height=1, width=15, command = casa_index).place(x=1000, y=150)
    casa_edit = Button(main_screen, text = "Editar casa", height=1, width=15).place(x=800, y=175)
    casa_delete = Button(main_screen, text = "Dar de baja", height=1, width=15).place(x=1000, y=175)

    Label(main_screen, text = "Paquetes",height=1, font=("Open Sans", 35)).place(x=675, y=200)

    paquete_new = Button(main_screen, text = "Agregar paquete", height=1, width=15).place(x=800, y=250)
    Button(main_screen, text = "Ver paquetes", height=1, width=15, command = paquete_index_propietario).place(x=1000, y=250)
    paquete_edit = Button(main_screen, text = "Editar paquete", height=1, width=15).place(x=800, y=275)
    paquete_delete = Button(main_screen, text = "Dar de baja", height=1, width=15).place(x=1000, y=275)

    Label(main_screen, text = "Reservas",height=1, font=("Open Sans", 35)).place(x=675, y=300)

    reservas_index = Button(main_screen, text = "Ver reservas", height=1, width=15, command = reserva_index_propietario).place(x=800, y=350)
    reserva_destroy = Button(main_screen, text = "Anular reservas", height=1, width=15, command = reserva_delete).place(x=1000, y=350)

    Label(main_screen, text = "Pagos",height=1, font=("Open Sans", 35)).place(x=675, y=375)

    Button(main_screen, text = "Agregar pago", height=1, width=15, command = pago_new).place(x=800, y=425)
    Button(main_screen, text = "Ver pagos", height=1, width=15, command = pago_index).place(x=1000, y=425)

    main_screen.mainloop()

main_screen()
