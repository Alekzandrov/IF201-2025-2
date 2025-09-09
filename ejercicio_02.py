import unittest
class Vehiculo():
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo
        
    def mostrar_info(self):
        return f'El vehiculo es de la \n marca {self.marca}, \n modelo {self.modelo}'   #\n es para que se ponga uno debajo de otro como en lista
    
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, num_puertas: int):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
        
    def es_deportivo(self) -> bool:
        return(self.num_puertas == 2)
        
        
        '''if(self.num_puertas == 2):
            return f'El vehiculo es deportivo'
        else:
            return f'El vehiculo no es deportivo'''
        
class TestPruebaAutomovil(unittest.TestCase):
    def setUp(self):
        self.auto1 = Automovil('Mazda', '3', 4)
        self.auto2 = Automovil('Ferrari', 'Z', 2)
    
    def test_auto_no_deportivo(self):
        self.assertFalse(self.auto1.es_deportivo())
        
    def test_auto_deportivo(self):
        self.assertTrue(self.auto2.es_deportivo())
        
    def test_auto_deportivo_2(self):
        self.assertEqual(self.auto2.es_deportivo(), True)
        
    def test_auto_deportivo_3(self):
        self.assertLess(self.auto2.num_puertas, 3)
        
if __name__ == '__main__':
    #unittest.main()   
    auto3 = Automovil('Honda', 'Accord', 2)
    if auto3.es_deportivo():
        print (auto3.mostrar_info() + '\n (Auto Deportivo)')
    else:
        print (auto3.mostrar_info() + '\n (auto sedan)')
    
    
    
    
    