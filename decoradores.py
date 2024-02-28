# Es una función que decora a otra
# Agrega un codigo extra a la función que ya existia 
# toma una función de entrada le agrega una funcionalidad extra y devuelve la función modificada

def decorador(funcion):
  def funcion_modificada():
    print("Antes de llamar a la función")
    funcion()
    print("Despues de llamar a la función")
  return funcion_modificada

def saludo():
  print("Hola, mundo!")

# saludo_modificado = decorador(saludo)
# saludo_modificado()
# saludo()


@decorador
def saludo():
  print("Hola, mundo!")

saludo()