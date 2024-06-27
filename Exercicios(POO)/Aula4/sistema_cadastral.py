# Princípio da responsabilidade única = cada função deve ser responsável por uma e somente uma função. Vejamos um exemplo abaixo:

class SistemaCadastral:

    def cadastrar(self, nome: str, idade: int) -> None:
        if self.__verificar_dados(nome, idade):
            self.__armazenar_usuario(nome, idade)
        else:
            self.__indicar_erro

    
    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False
    

    def __armazenar_usuario(self, nome: str, idade: int) -> None:
        print('Acessando o banco de dados...')
        print('Cadastrar o usuário {}, idade {}'. format(nome, idade))
    

    def __indicar_erro(self) -> None:
        print('Dados inválidos!')

# Perceba como no algoritmo acima cada função é responsável por uma única responsabilidade. Poderiamos modularizar ainda mais o nosso código, criando classes para serem responsáveis por cada uma dessas funções especificamente. 