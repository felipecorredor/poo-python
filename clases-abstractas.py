# Una clase abstracta es una clase que nos permite tener abstracción 
# Ocultar la complejidad interna de un sistema

# abstractclassmethod es un decorador

from abc import ABC, abstractmethod

class Persona(ABC):
    def __init__(self, nombre, sexo, actividad, edad=None):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad

    @abstractmethod
    def hacer_actividad(self):
        pass

    def presentarse(self):
        if self.edad is not None:
            print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
        else:
            print(f"Hola, me llamo {self.nombre}.")

class Estudiante(Persona):
    def __init__(self, nombre, sexo, actividad, edad=None):
        super().__init__(nombre, sexo, actividad, edad)

    def hacer_actividad(self):
        print(f"Estoy estudiando {self.actividad}.")

class Empleado(Persona):
    def __init__(self, nombre, sexo, actividad, edad=None):
        super().__init__(nombre, sexo, actividad, edad)

    def hacer_actividad(self):
        print(f"Trabajo como ingeniero en {self.actividad}.")

# persona = Persona("Felipe", 23, "M") # Error porque no se puede crear una clase abstracta

# Ejemplo de uso
estudiante = Estudiante("Felipe", "M", "programacion", 23)
empelado = Empleado("Juan", "M", "programacion")

estudiante.presentarse()
# estudiante.hacer_actividad()

empelado.presentarse()
# empelado.hacer_actividad()
