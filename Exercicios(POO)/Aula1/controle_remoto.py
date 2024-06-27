class ControleRemoto:

    def __init__(self, televisao, comodo) -> None:
        self.televisao = televisao
        self.comodo = comodo

    
    def avancar_canal(self):
        print('Avançando canal...')

    
    def voltar_canal(self):
        print('Voltando o canal...')

    
    def escolher_canal(self, canal):
        print('Canal alterado para: {}'.format(canal))


controle_sala = ControleRemoto('Samsung', 'Sala')
print(controle_sala.comodo)
print(controle_sala.televisao)
controle_sala.avancar_canal()

controle_quarto = ControleRemoto('LG', 'quarto')
controle_quarto.comodo
controle_quarto.televisao
controle_quarto.escolher_canal(15)