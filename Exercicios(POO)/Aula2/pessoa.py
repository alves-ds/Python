class Pessoa:

    def __init__(self, nome, idade, cpf) -> None:
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf # Vão existir situações nas quais não queremos que o objeto acesse algumas variáveis. Podemos torná-las privadas utilizando-se de __. Isso fará com que a variável seja acessível somente no contexto da classe.

    
    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('Bebendo...')

    
    def correr(self):
        print('Correndo...')
    

    def __apresentar_documento(self): # Também podemos criar métodos privados, que serão acessíveis somente no contexto da classe, porém não pelo objeto. 
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 25, '254ashdjahsjdbadba')
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')