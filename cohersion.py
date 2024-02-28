num1 = 3
num2 = 4.6

resultado = num1 + num2

print(type(num1))
print(type(resultado))
print(resultado)

def recorrer(elementos):
  for item in elementos:
    print(f"el elemento actual es: {item}")

lista = [1, 2, 3, 4, 5]
lista2 = ["Hola", "Mundo", "!"]
lista3 = "Hola" 

recorrer(lista)
recorrer(lista2)