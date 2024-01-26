import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

ventana = tk.Tk()
ventana.title("Hola desde Python3")
ventana.geometry("600x400")

frame = ttk.LabelFrame(ventana, text='Título Frame', width=385, height=200, borderwidth=5, relief="raised")

frame.grid(row=1, column=0)

etiqueta = tk.Label(frame, text='Titulo', font=('Arial',12,'bold')) # Insertándo un título en la ventana
etiqueta.grid(row=3, column=0)

imagen_pil = Image.open("logo.jpg")
imagen_tk = ImageTk.PhotoImage(imagen_pil)
label_img = tk.Label(frame, image=imagen_tk)
label_img.grid(row=5,column=0)

ventana.mainloop() # El main loop solo puede existir una vez en una aplicación tkinter


