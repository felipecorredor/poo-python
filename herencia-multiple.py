class Persona: 
  def __init__(self, nombre, edad, nacionalidad):
    self.nombre = nombre
    self.edad = edad 
    self.nacionalidad = nacionalidad

  def hablar(self):
    return "Hola, estoy hablando"

class Empleado(Persona):
  def __init__(self, nombre, edad, nacionalidad, trabajo, salario):
    super().__init__(nombre, edad, nacionalidad)
    self.trabajo = trabajo
    self.salario = salario

class Estudiante(Persona):
  def __init__(self, nombre, edad, nacionalidad, universidad):
    super().__init__(nombre, edad, nacionalidad)
    self.universidad = universidad

class Artista:
  def __init__(self, habilidad):
    self.habilidad = habilidad

  def mostrar_habilidad(self):
    return f"mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
      Persona.__init__(self, nombre, edad, nacionalidad)
      Artista.__init__(self, habilidad)

      self.salario = salario
      self.empresa = empresa
    
    def presentarse(self):
      # Con super hereda el método de la clase padre
      return f"Hola, soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo en {self.empresa}"

empelado = Empleado("felipe", 23, "colombiano", "Programador", 3299823)
print(empelado.hablar())

estudiante = Estudiante("juan", 23, "peruano", "UM")
print(estudiante.universidad)

empleadoArtista = EmpleadoArtista("felipe", 23, "colombiano", "Cantar", 23299823, "WizeLine")

print(empleadoArtista.presentarse()) 

herencia = issubclass(EmpleadoArtista, Artista)
print("herencia", herencia)

instancia = isinstance(empleadoArtista, EmpleadoArtista)
print("instancia", instancia)

