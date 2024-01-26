import tkinter as tk 
from PIL import Image, ImageTk

def saludo():
    print("Hola desde el botón")

ventana = tk.Tk()
ventana.title("Hola desde Python")
ventana.geometry("600x400")

etiqueta = tk.Label(ventana, text='Título de la ventana', fg="#ffffff", bg="blue") # Insertándo un título en la ventana
# etiqueta.pack(fill=tk.X, expand=True) # Ubicar el texto en el eje Y
# etiqueta.pack(side=tk.LEFT) # Ubicar el texto en el eje X 
# etiqueta.pack(fill=tk.BOTH, expand=True) # Para que el cuadro de texto ocupe todo el espacio
etiqueta.pack() # Cargando el título

boton = tk.Button(ventana, text="Presiona aquí", command=saludo) # Agregando un botón a la ventana
boton.pack() # Cargando el botón

# Cargar la imagen con Pillow
imagen_pil = Image.open("logo.jpg")

# Convertir la imagen a un formato compatible con Tkinter
imagen_tk = ImageTk.PhotoImage(imagen_pil)

# Agregar la imagen a la etiqueta y mostrarla
label_img = tk.Label(ventana, image=imagen_tk)
label_img.pack()


ventana.mainloop()

