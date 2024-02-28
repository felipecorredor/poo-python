class MiClase:
  def __init__(self):
    self._atributo_privado = "Valor"
    self.__atributo_muy_privado = "Muy privado"

  def __hablar(self):
    print("Hola, estoy hablando")

  def hablar_publico(self):
    self.__hablar()

objeto = MiClase();

print(objeto._atributo_privado) # el desarrollador entiende que es un atributo privado pero si quiere puede acceder
# print(objeto.__atributo_muy_privado) # no lo encuentra porque es privado

# A pesar de esto, todavía hay una forma de acceder a los atributos "privados" en Python utilizando una convención de nombres llamada "name mangling" (mezclado de nombres).
print(objeto._MiClase__atributo_muy_privado) # Salida: Muy privado

objeto._MiClase__hablar()  # Salida: Hola, estoy hablando
