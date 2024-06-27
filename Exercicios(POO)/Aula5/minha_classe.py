# Trabalhando com variáveis de classe

class MinhaClasse:

    estatico = 'Douglas' # Variável de classe

    def __init__(self, estado: bool) -> None:
        self.estado = estado
    
    def print_estatico(self):
        print(self.estatico)
    
    @classmethod
    def mudar_estatico(cls):
        cls.estatico = 'Programador'


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)

obj1.mudar_estatico()

obj1.print_estatico()
obj2.print_estatico()