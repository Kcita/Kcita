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

global main_screen
global Kcita

kcita = Kcita("Kcita")

def sign_in_verify():
    usuario = usuario_verify.get()
    password = password_verify.get()
    print("hola")
    success = kcita.iniciar_sesion(usuario, password)

def sign_in_screen():
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

def cerrar_sesion():
    kcita.salir_sesion()

def sign_up_screen():
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
    Button(sign_up_screen, text="Resgitrarse", width=10, height=1, command = registrarse).pack()

def main_screen():
    main_screen = Tk()
    main_screen.geometry("1250x750")
    main_screen.title("Kcita: reserva de dormitorios y casas")

    titulo_cliente = Label(main_screen, text = "Cliente",height=1, width=15 , font="Times 40")
    titulo_cliente.place(x=150, y=10)

    titulo_propietario = Label(main_screen, text = "Propietario",height=1, width=15 , font="Times 40")
    titulo_propietario.place(x=750, y=10)

    #Boton de logeo de propietario
    sign_in = Button(main_screen, text = "Iniciar sesión", height=1, width=15, command=sign_in_screen)
    sign_in.place(x=700, y=75)

    sign_up = Button(main_screen, text = "Registrarse", height=1, width=15, command=sign_up_screen)
    sign_up.place(x=850, y=75)

    log_out = Button(main_screen, text = "Cerrar sesión", height=1, width=15, command=cerrar_sesion)
    log_out.place(x=1000, y=75)

    Label(main_screen, text = "Casas",height=1, font="Times 40").place(x=675, y=100)

    casa_new = Button(main_screen, text = "Agregar casa", height=1, width=15).place(x=800, y=150)
    casa_index = Button(main_screen, text = "Ver casas", height=1, width=15).place(x=1000, y=150)
    casa_edit = Button(main_screen, text = "Editar casa", height=1, width=15).place(x=800, y=175)
    casa_delete = Button(main_screen, text = "Dar de baja", height=1, width=15).place(x=1000, y=175)

    Label(main_screen, text = "Casas",height=1, font="Times 40").place(x=675, y=100)

    casa_new = Button(main_screen, text = "Agregar casa", height=1, width=15).place(x=800, y=150)
    casa_index = Button(main_screen, text = "Ver casas", height=1, width=15).place(x=1000, y=150)
    casa_edit = Button(main_screen, text = "Editar casa", height=1, width=15).place(x=800, y=175)
    casa_delete = Button(main_screen, text = "Dar de baja", height=1, width=15).place(x=1000, y=175)

    main_screen.mainloop()

main_screen()
