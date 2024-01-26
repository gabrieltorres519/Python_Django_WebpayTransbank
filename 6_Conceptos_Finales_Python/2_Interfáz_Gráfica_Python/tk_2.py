import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Hola desde Python3")
ventana.geometry("600x400")

etiqueta = tk.Label(ventana, text='Ingresa tu nombre') # Insertándo un título en la ventana
etiqueta.pack() # Cargando el título

etiqueta2 = tk.Label(ventana, text='') # Creando etiqueta para empacarla después del botón
# La empacaremos después del botón para que al presionarlo recien nos aparesca el texot del label

campo = tk.Entry(ventana) # Agregando campo para ingresar texto
campo.pack()

def procesar(): 
    texto = campo.get()
    etiqueta2['text'] = texto # Agregando el texto deseado a etiqueta2

boton = tk.Button(ventana, text="Enviar", command=procesar)
boton.pack()

etiqueta2.pack() # Mostrando el texto de la etiqueta

ventana.mainloop()
