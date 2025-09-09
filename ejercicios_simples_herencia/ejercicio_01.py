class persona():
    def __init__(self, nombre: str, edad: int):
         self.nombre = nombre
         self.edad = edad 

    def presentarse(self):
        return f'Hola, soy {self.nombre}, y tengo {self.edad} años'

class Estudiante(persona):
    def __init__(self, nombre: str, edad: int, carrera: str ):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def presentarse(self):
        return super().presentarse() + f' y estudio la carrera de {self.carrera}'

if __name__ == '__main__':
    objEst = Estudiante('Inguncha', 21, 'Ing informatica')
    print(objEst.presentarse())