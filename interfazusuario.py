from tkinter import *

ventana = Tk()
ventana.title("Mi Ventana")
ventana.geometry("800x600")

etiqueta = Label(ventana, text="Esto es una etiqueta")
etiqueta.pack()

segundaEtiqueta = Label(ventana, text="Segunda etiqueta")
segundaEtiqueta.pack()

ingresoTexto = Entry(ventana)
ingresoTexto.pack()

boton = Button(ventana, text="Mi boton")
boton.pack()


ventana.mainloop()