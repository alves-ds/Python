# Ao criar classes, para acessar seus atributos, uma abordagem interessante é a utilização de "getters" e "setters", como no exemplo abaixo:

class Alarme:

    def __init__(self, estado: bool) -> None:
        self.__estado = estado

    def get_estado(self) -> bool:
        return self.__estado
    
    def set_estado(self, valor: bool) -> None:
        if isinstance(valor, bool):
            self.__estado = valor

