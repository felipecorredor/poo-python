# Que es lo que mas prioridad tiene
# MRO (Método de resolución de orden) hace referencia a el orden en el que python busca métodos y atributos en una clase

class A:
  def hablar(self):
    print("Hola desde A")

class B(A):
  def hablar(self):
    print("Hola desde B")

class C:
  def hablar(self):
    print("Hola desde C")
  
class D(B, C): 
  def hablar(self):
    print("Hola desde D")

d = D()

print(D.mro())
d.hablar()

# si se quiere ejecutar el método hablar de la clase B y pasar un objeto
# para que lo tome como self
B.hablar(d)