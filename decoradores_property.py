class Persona:
  def __init__(self, nombre, edad):
    self.__nombre = nombre
    self.edad = edad
  

  @property
  def nombre(self):
    return self.__nombre
  
  @nombre.setter
  def nombre(self, new_nombre):
    self.__nombre = new_nombre

  # Elimina valores
  @nombre.deleter
  def nombre(self):
    del self.__nombre

persona = Persona("Pepito", 23)
nombre = persona.nombre
print(nombre)

persona.nombre = "Juan"
nombre = persona.nombre
print(nombre)


del persona.nombre
# nombre = persona.nombre # Error porque ya se elimino esa propiedad
print("nombre")