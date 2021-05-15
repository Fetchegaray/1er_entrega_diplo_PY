# Importamos todas las Bibliotecas con las que vamos a trabajar
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import re

# Se crea la aplicación
raiz = Tk()
raiz.title(
    "Campaña vacunación contra el Covid-19 | Ingresar a los nuevos inscriptos")
raiz.geometry("1100x350")
raiz.resizable(False, False)

myId = StringVar()
myname = StringVar()
myaddress = StringVar()
mydateofbirth = StringVar()
myemail = StringVar()
mycity = StringVar()

# Conectar a base de datos y creación de la misma


def connectdatabase():
    myconecction = sqlite3.connect("base.db")
    mycursor = myconecction.cursor()

    try:
        mycursor.execute('''
            CREATE TABLE registro (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50) NOT NULL,
            DOMICILIO VARCHAR(50) NOT NULL,
            FECHANAC VARCHAR(50) NOT NULL,
            CORREOELEC VARCHAR(50) NOT NULL,
            LUGARR VARCHAR(50) NOT NULL)
            ''')
        messagebox.showinfo("CONEXION", "Base de datos Creada")
    except:
        messagebox.showinfo(
            "CONEXION", "Conexión exitosa con la base de datos")

# Elimina toda la base de datos: cuidado con ejecutarla porque se ordena su borrado completo


def eliminardatabase():
    myconecction = sqlite3.connect("base.db")
    mycursor = myconecction.cursor()
    if messagebox.askyesno(message="Los datos se perderan definitivamente ¿desea continuar de todos modos?", title="ADVERTENCIA"):
        mycursor.execute("DROP TABLE registro")
    else:
        pass
    limpiarCampos()
    mostrar()


def exitapp():
    valor = messagebox.askquestion(
        "Salir", "¿Está seguro que desea salir de la app?")
    if valor == "yes":
        raiz.destroy()


def limpiarCampos():
    myId.set("")
    myname.set("")
    myaddress.set("")
    mydateofbirth.set("")
    myemail.set("")
    mycity.set("")


def mensaje():
    acerca = '''
    Aplicación Grafica con database SQlite3
    Version 1.0
    Tegnología Python Tkinter
    '''
    messagebox.showinfo(title="INFORMACION", message=acerca)

# Metodos CRUD


def crear():
    myconecction = sqlite3.connect("base.db")
    mycursor = myconecction.cursor()
    try:
        date = myname.get(), myaddress.get(), mydateofbirth.get(), myemail.get(), mycity.get()
        veriftxt(date)
        veriffecha(date)
        verifmail(date)
        verifdir(date)
        mycursor.execute("INSERT INTO registro VALUES(NULL,?,?,?,?,?)", (date))
        myconecction.commit()
    except:
        messagebox.showwarning(
            "ADVERNTENCIA", "Ocurrió un error al crear el registro, verifique conexión con base de datos")
        pass
    limpiarCampos()
    mostrar()


def mostrar():
    myconecction = sqlite3.connect("base.db")
    mycursor = myconecction.cursor()
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)

    try:
        mycursor.execute("SELECT * FROM registro")
        for row in mycursor:
            tree.insert("", 0, text=row[0], values=(
                row[1], row[2], row[3], row[4], row[5]))
    except:
        pass


# Tabla

tree = ttk.Treeview(height=10, columns=('#0', '#1', '#2', '#3', '#4', '#5'))
tree.place(x=0, y=130)
tree.column('#0', width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre completo", anchor=CENTER)
tree.heading('#2', text="Domicilio", anchor=CENTER)
tree.heading('#3', text="Fecha de nacimiento", anchor=CENTER)
tree.heading('#4', text="Correo electrónico", anchor=CENTER)
tree.heading('#5', text="Lugar de recidencia actual", anchor=CENTER)


def selecionarClick(event):
    item = tree.identify('item', event.x, event.y)
    myId.set(tree.item(item, "text"))
    myname.set(tree.item(item, "values")[0])
    myaddress.set(tree.item(item, "values")[1])
    mydateofbirth.set(tree.item(item, "values")[2])
    myemail.set(tree.item(item, "values")[3])
    mycity.set(tree.item(item, "values")[4])


tree.bind("<Double-1>", selecionarClick)


def actualizar():
    myconecction = sqlite3.connect("base.db")
    mycursor = myconecction.cursor()

    try:
        date = myname.get(), myaddress.get(), mydateofbirth.get(), myemail.get(), mycity.get()
        veriftxt(date)
        veriffecha(date)
        verifmail(date)
        verifdir(date)
        myIdint = str(myId.get())
        mycursor.execute("UPDATE registro SET NOMBRE= ?, DOMICILIO= ?, FECHANAC= ?, CORREOELEC= ?, LUGARR= ? WHERE ID= ?",
                         (date[0], date[1], date[2], date[3], date[4], myIdint))
        myconecction.commit()
    except:
        messagebox.showwarning(
            "ADVERNTENCIA", "Ocurrió un error al actualizar el registro")
        pass
    limpiarCampos()
    mostrar()


def borrar():
    myconecction = sqlite3.connect("base.db")
    mycursor = myconecction.cursor()
    try:
        if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="ADVERTENCIA"):
            mycursor.execute("DELETE FROM registro WHERE ID="+myId.get())
            myconecction.commit()
    except:
        messagebox.showwarning(
            "ADVERTENCIA", "Ocurrió un error al intentar borrar el registro")
        pass
    limpiarCampos()
    mostrar()

# Comienzo de las funciones para validar los campos


def veriftxt(tupdatostxt):
    reg = re.compile(r"^[A-Za-z.-]+(\s*[A-Za-z.-]+)*$")
    if reg.match(tupdatostxt[0]) and reg.match(tupdatostxt[4]) is not None:
        pass
    else:
        messagebox.showwarning(
            "Advertencia", "Los campos Nombre y Lugar de residencia solo pueden contener letras y no estar vacios")
        raise ("Error")


def veriffecha(tupdatosfech):
    reg = re.compile(r"^(0[1-9]|[1-2][0-9]|3[0-1])\/(0[1-9]|1[0-2])\/(\d{4})$")
    if reg.match(tupdatosfech[2]) is not None:
        pass
    else:
        messagebox.showwarning(
            "Advertencia", "El campo fecha de nacimiento solo acepta formato DD/MM/AAAA")
        raise ("Error")


def verifmail(tupdatosmail):
    reg = re.compile(
        r"^((\w[^\W]+)[\.\-]?){1,}\@(([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$")
    if reg.match(tupdatosmail[3]) is not None:
        pass
    else:
        messagebox.showwarning(
            "Advertencia", "El campo E-mail es debe tener la forma mail@servidor.com")
        raise ("Error")

# No tenia sentido usar un regex para validar que no estuviera vacia.


def verifdir(tupdatosdir):
    if tupdatosdir[1] != "":
        pass
    else:
        messagebox.showwarning(
            "Advertencia", "El campo Direccion no puede estar vacio")
        raise ("Error")

# Fin de las funciones de validacion de los campos


# Colocar elementos en la ventana
# Creación de los menus
menubar = Menu(raiz)
raiz.config(menu=menubar)

menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(
    label="Crear / Conectar base de datos", command=connectdatabase)
menubasedat.add_command(label="Eliminar base de datos",
                        command=eliminardatabase)
menubasedat.add_command(label="Salir", command=exitapp)
menubar.add_cascade(label="Inicio", menu=menubasedat)

ayudamenu = Menu(menubar, tearoff=0)
ayudamenu.add_command(label="Resetear Campos", command=limpiarCampos)
ayudamenu.add_command(label="Acerca", command=mensaje)
menubar.add_cascade(label="Ayuda", menu=ayudamenu)

# Creación de las etiquetas y cajas de texto
e1 = Entry(raiz, textvariable=myId)

l2 = Label(raiz, text="Nombre completo")
l2.grid(row=0, column=0)
e2 = Entry(raiz, textvariable=myname, width=25)
e2.focus()
e2.grid(row=0, column=1)

l3 = Label(raiz, text="Domicilio")
l3.grid(row=1, column=0)
e3 = Entry(raiz, textvariable=myaddress, width=25)
e3.grid(row=1, column=1)

l4 = Label(raiz, text="Fecha de nacimiento")
l4.grid(row=0, column=2)
e4 = Entry(raiz, textvariable=mydateofbirth, width=25)
e4.grid(row=0, column=3)

l5 = Label(raiz, text="Correo electrónico")
l5.grid(row=1, column=2)
e2 = Entry(raiz, textvariable=myemail, width=30)
e2.grid(row=1, column=3)

l6 = Label(raiz, text="Lugar de recidencia actual")
l6.grid(row=0, column=4)
e2 = Entry(raiz, textvariable=mycity, width=25)
e2.grid(row=0, column=5)

# Creación de los botones
b1 = Button(raiz, text="Cargar Registro", command=crear)
b1.place(x=50, y=90)
b2 = Button(raiz, text="Modificar Registro", command=actualizar)
b2.place(x=180, y=90)
b3 = Button(raiz, text="Mostrar Lista", command=mostrar)
b3.place(x=320, y=90)
b4 = Button(raiz, text="Eliminar Registro", command=borrar)
b4.place(x=450, y=90)

raiz.mainloop()
