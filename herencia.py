class Persona: 
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad 
    self.nacionalidad = nacionalidad

  def hablar(self):
    print("Hola, estoy hablando un poco")

class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario

class Estudiante(Persona):
  def __init__(self, nombre, edad, nacionalidad, universidad):
    super().__init__(nombre, edad, nacionalidad)
    self.universidad = universidad


empelado = Empleado("felipe", 23, "colombiano", "Programador", 3299823)
print(empelado.hablar())

estudiante = Estudiante("juan", 23, "peruano", "UM")
print(estudiante.universidad)