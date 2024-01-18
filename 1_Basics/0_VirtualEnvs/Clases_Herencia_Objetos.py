class Padre():

    def retornarTexto(self):
        return "Hola soy la clase padre"
    
# Herencia trabaja bajo el concepto de clase padre y clase hijo 
# y tabién está el concepto de colaboración de objetos.

class Hija(Padre): # De ésta forma indicamos la herencia de todo lo contenido en la clase padre

    def miMetodo(self):
        saludo_padre = self.retornarTexto() # Usando un mpetodo de la clase padre
        saludo_hija = " agregando extra texto en clase hija"
        return saludo_padre + saludo_hija

hija = Hija()

print(hija.retornarTexto()) # Un muy buen ejemplo del uso de clases, sus métodos y el concepto 
                            # de herencia es cuando se trabaja con APIs
print(hija.miMetodo())



