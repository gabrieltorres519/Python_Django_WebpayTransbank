# Concepto de colaboración de objetos.

class Padre():

    def retornarTexto(self):
        return "It's an equivalent exchange!!!"


class Hija(): 

    def __init__(self):
        self.p=Padre() # Éste atributo de la clase es una instancia de la clase Padre()

    def miMetodo(self):
        return self.p.retornarTexto() # Usando un método de la case llamada Padre() 
                                      # pero sin ser herencia o realmente una clase hija

hija = Hija()
# print(hija.retornarTexto()) causaría un error ya que no es herencia, no contamos con los 
# métodos de la clase Padre() en realidad

print(hija.miMetodo()) 