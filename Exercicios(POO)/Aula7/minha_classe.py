# Nessa aula, vimos como fazer uma classe interagir com outra. Vejamos isso no exemplo abaixo:

from typing import Type

class Interruptor:

    def __init__(self, comodo) -> None:
        self.__comodo = comodo

    def acender(self):
        print('Acendendo o {}'.format(self.__comodo))

    def apagar(self):
        print('Apagando o {}'.format(self.__comodo))


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: type[Interruptor]):
        interruptor.apagar()
    
    def dormir(self):
        print('Fui dormir...')


Douglas = Pessoa()
interruptor_quarto = Interruptor('quarto')

Douglas.acender_luz(interruptor_quarto)