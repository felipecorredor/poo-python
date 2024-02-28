class Animal():
  def comer(self):
    print("El animal esta comiendo")

class Ave(Animal):
  def volar(self):
    print("El Ave esta volando")

class Mamifero(Animal):
  def amamantar(self):
    print("El mamimero se está amamantando")


class Murcielago(Mamifero, Ave):
  pass

murcielago =  Murcielago()

murcielago.amamantar()
murcielago.volar()
murcielago.comer()

