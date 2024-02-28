# Formas de acceder y modificar los valores de una clase

class Persona:
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.edad = edad
  
  def set_nombre(self, new_nombre):
    self.__nombre = new_nombre

  def get_nombre(self):
    return self.__nombre


# No deberiamos hacerlo de esta forma ya que tenemos los atributos privados
persona = Persona("Lucas", 23)
nombre = persona.get_nombre()
print(nombre)

persona.set_nombre("Juan")
nombre2 = persona.get_nombre()
print(nombre2)