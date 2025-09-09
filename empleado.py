from abc import ABC, abstractmethod     #ABC pemite gestionar clases de caracteristicas abstractas

class Empleado(ABC):
    def __init__(self, nombre: str, salario_base: float):      # __init es el constructor/metodo que puede crear objetos
        self.nombre = nombre
        self.salario_base = salario_base     #self indica que estamos declarando un atributo de la clase 
           
    def calcular_salario(self) -> float:
        return self.salario_base 
        # -> es para indicar el valor que se quiere retornar gaaa 
    
    def mostrar_informacion(self):
        print(f'Empleado: {self.nombre} | Salario base: {self.salario_base}')

if __name__ == '__main__':
    obj = Empleado('juan', 1000)
    obj.mostrar_informacion()