# Aula sobre polimorfismo. Explicação simplista: com o polimorfismo podemos criar classes que herdam atributos e métodos de outra classe, porém modificar uma dessas classes herdadas, mudando assim a sua funcionalidade. Vejamos um exemplo:

class Mae:

    def __init__(self) -> None:
        return None
    
    def trabalhar(self) -> None:
        print('Eu tenho um trabalho!')

class Filha(Mae):

    def __init__(self) -> None:
        super().__init__()
    
    def trabalhar(self) -> None:
        print('Eu não posso trabalhar, não possuo idade para isso!') # Mesmo herdando o metodo da classe Mae, consigo modifica-lo para essa nova classe. 


mae = Mae()
filha = Filha()

mae.trabalhar()
filha.trabalhar()


