from empleado import Empleado

class Empleado_tiempo_completo(Empleado):
    def __init__(self, nombre: str, salario_base: float, bono: float):
        super().__init__(nombre, salario_base)           #super().__init__ es para referirse al constructor base 
        self.bono = bono
        
    def calcular_salario(self) -> float:
        return super().calcular_salario() + self.bono
    
if __name__ == '__main__':
    emp = Empleado_tiempo_completo('Inguncha', 1000, 33)
    emp.mostrar_informacion()
    print(f'El salario de este kbro es de: {emp.calcular_salario()}')   # el calcular_salario le pones () al final porque es una funcion
    