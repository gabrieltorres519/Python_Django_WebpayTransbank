import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

ventana = tk.Tk()
ventana.title("Hola desde Python3")
ventana.geometry("600x400")

boton1 = tk.Button(ventana, text="Botón 1", width=10, height=5 )
boton2 = tk.Button(ventana, text="Botón 2", width=10, height=5 )
boton3 = tk.Button(ventana, text="Botón 3", width=10, height=5 )

# Cargar la imagen con Pillow
imagen_pil = Image.open("logo.jpg")
# Convertir la imagen a un formato compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_pil)
# Agregar la imagen a la etiqueta y mostrarla
label_img = tk.Label(ventana, image=imagen_tk)

boton1.grid(row=0, column=0)
boton2.grid(row=0, column=1)
boton3.grid(row=0, column=2)
label_img.grid(row=0, column=3)



ventana.mainloop() # El main loop solo puede existir una vez en una aplicación tkinter
