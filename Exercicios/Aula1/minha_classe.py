# Classes podem ser pensadas como abstrações de coisas que existem na vida real, possuindo assim atributos (instâncias) e métodos. 

class MinhaClasse: # Para criar uma classe, utilizamos a palavra reservada "class"

    def __init__(self, att) -> None: # Posso também definir para o usuário fornecer atributos para a classe, utilizando um método construtor
        self.meu_atributo = 'Ola python'
        self.meu_atributo2 = att

    def meu_metodo(self): #Sempre que criamos um método em uma classe, precisamos identificar que este método pertence à classe. Fazemos isso utilizando o parâmetro "self"
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult):
        print(num * mult) 


objeto = MinhaClasse(23) # Não utilizamos classes diretamente. Para isso, precisamos criar objetos, pelos quais utilizamos as classes. 
objeto.meu_metodo()
objeto.meu_metodo2(3,6)