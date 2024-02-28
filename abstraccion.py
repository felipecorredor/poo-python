# Manejar la complejidad ocultando todos los detalles innecesarios al programador o al usuario 
# Crear una interfaz simple que oculte la interfaz compleja 

# no necesitas saber como funciona internamente
# Si no que necesitas saber como usarlo

class Auto():
  def __init__(self):
    self._estado = "apagado"

  def encender(self):
    self._estado = "encendido"
    print("El auto está encendido")

  def conducir(self):
    if self._estado == "apagado":
      self.encender()

    print(f"Conduciendo el auto")
    
auto = Auto() # Auto automatico
auto.conducir()