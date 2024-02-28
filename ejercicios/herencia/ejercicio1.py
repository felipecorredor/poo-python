# Crear un clase estudiante

# Agregar atributos name, age y grade

class Student: 
  def __init__(self, name, age, grade) -> None:
    self.name = name
    self.age = age
    self.grade = grade

felipe = Student("Felipe", 24, 8)

print(felipe.name)