# Interactuar con el usuario y debe brindar los atributos

# Agregar método estudiar "el estudiante(nombre) está estudiando"

# Crear un objeto Student

# Usar el método Student

class Student: 
  def __init__(self, name: str, age: int, grade: str) -> None:
    self.name = name
    self.age = age
    self.grade = grade

  def studying(self, isOlder: int):
    if (isOlder):
      print(f"The student {self.name} is studying" )
    else:
      print(f"The student is not student" )


name = input("What is your name: ")
age = input("What is your age: ")
grade = input("What is your grade: ")

student = Student(name, age, grade)

student.studying(False)