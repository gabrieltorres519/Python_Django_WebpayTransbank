import tkinter as tk 
from PIL import Image, ImageTk
from tkinter import messagebox, ttk

# Para convertir esta pequeña aplicación en un ejecutable 
# instala pip install pyinstaller y en la terminal 
# utiliza el comando con el nombre del archivo que quieres
# convertir en ejecutable, donde esté corriendo el método 
# mainloop - > pyinstaller tkinter_ejemplo_final.py

ventana = tk.Tk()
ventana.title("Hola desde Python3")

etiqueta = tk.Label(ventana, text='Listado de Ítems', font=('Arial',12,'bold')) # Insertándo un título en la ventana
etiqueta.grid(row=0, column=0)

tabla = ttk.Treeview(ventana, columns=('Nombre, Email, Teléfono'))
tabla.grid(row=1,column=0,sticky="nse")

scroll = ttk.Scrollbar(ventana, orient="vertical", command=tabla.yview)

scroll.grid(row=5, column=4, sticky="nse")

tabla.configure(yscrollcommand=scroll.set)

tabla.heading("#0", text="ID")
tabla.heading("#1", text="Nombre")
tabla.heading("#2", text="Email")
tabla.heading("#3", text="Teléfono")

for i in range(1,100):
    tabla.insert('', 0, text=f"{i}", values=("Gabriel Torres", 'gabrieltorres9909@gmail.com', '445845678'))



ventana.mainloop() 