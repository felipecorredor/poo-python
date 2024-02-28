# Es un concepto que hace referencia a poder enviar un mensaje sintáctico a diferentes objetos
# pero el mensaje es el mismo pero el resultado que tiene que generar es distinto

class Gato():
  def sonido(self):
    return "Miau"
  
class Perro():
  def sonido(self):
    return "Guau"
  
gato = Gato()
perro = Perro();

# un tipo de polimorfismo
gato = print(gato.sonido()) 
perro = print(perro.sonido())