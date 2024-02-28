# # Clases y Objetos

# # Atributos estáticos
# class Persona():
#   nombre = "Felipe"
#   edad = 23
#   genero = "Masculino"


# # Instancia de la clase 
# persona = Persona()
# persona.nombre = "Juan"
# print(persona.nombre)


class Persona:
  def __init__(self, nombre, edad, genero):
    self.nombre = nombre
    self.edad = edad
    self.genero = genero

  def caminar(self):
    print(f"{self.nombre} Esta caminando")

  def comer(self):
    print(f"{self.nombre} Esta comiendo")

persona = Persona("Felipe", 24, "Masculino")

persona.caminar()



