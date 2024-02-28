# Es un concepto que hace referencia a poder enviar un mensaje sintáctico a diferentes objetos
# pero el mensaje es el mismo pero el resultado que tiene que generar es distinto

class Gato():
  def sonido(self):
    return "Miau"
  
class Perro():
  def sonido(self):
    return "Guau"
  
def hacer_sonido(animal):
  print(animal.sonido())
  
  
gato = Gato()
perro = Perro();

hacer_sonido(gato)
hacer_sonido(perro)

# un tipo de polimorfismo
# sonido = print(perro.sonido())