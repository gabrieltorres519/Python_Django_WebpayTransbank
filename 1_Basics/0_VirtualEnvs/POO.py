# Recordemos la llamada a funciones (funciones de python que hacen algo) dentro de modulos (archivos .py) 
# y la llamada a modulos (archivos .py con todas sus funciones) dentro de un paquete (carpeta con archivos .py),
# una clase viene siendo como un módulo que almacena funciones (métodos) y variables o constantes (atributos)

# Cómo crear una clase en python

class Persona:

    # Atributos
    nombre = "Cesar"
    # Constructor
    def __init__(self, nombre, appellido):
        self.nombre = nombre
        self.appellido = appellido
        self.edad = 24
    # Métodos
    def obtenerNombre(self, parametro):
        return f"nombre es {self.nombre}, parámetro es {parametro}"

# Creación de instancia 
    
persona = Persona("Gabriel","Torres")

# obtención de datos de la clase 

print(persona.edad) 
print(persona.obtenerNombre("hola"))

# verificar si una variable es instancia de alguna clase específica, esto es necesario porque luego 
# toca crear clases con demasiados métodos y no sabemos cuál es instancia de cuál, así que lo investigamos 
# con:

print(isinstance(persona, Persona))