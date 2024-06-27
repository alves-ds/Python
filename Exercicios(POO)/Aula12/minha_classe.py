# Exemplo sobre herança

class Mae:

    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = 'Silva'

    def comer(self) -> None:
        print('Estou comendo!')
    
    def estudar(self) -> None:
        print('Estou estudando!')

    
class Filha(Mae):

    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)
    
    def brincar(self, brinquedo: str) -> None:
        print('Estou brincando com {}'.format(brinquedo))

ana = Mae('Rua das pipas')
clara = Filha('Rua dos bairros')

clara.comer()