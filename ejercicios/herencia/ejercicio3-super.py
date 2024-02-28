class Persona():
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def mostrar_datos(self):
    print(f"El nombre del estudiante es {self.nombre} y su edad es {self.edad}")

class Estudiante(Persona):
  def __init__(self, nombre, edad, grado):
    super().__init__(nombre, edad)
    self.grado = grado
  
  def mostrar_grado(self):
    print(f"El grado del estudiante {self.nombre} es {self.grado}")


estudiante = Estudiante("Felipe", 23, 10)

estudiante.mostrar_datos()
estudiante.mostrar_grado()
