import operacoes

class Calculadora:

    def __init__(self) -> None:
        self.operacao = None
        self.num1 = None
        self.num2 = None


    def executar(self):
        self.exibir_instrucao()
        self.solicitar_info()
        self.verificar_op()


    def verificar_op(self):
        if self.operacao == 1:
            somado = operacoes.soma.somar(self.num1, self.num2)
            print(somado)
        
        elif self.operacao == 2:
            subtraido = operacoes.subtracao.sub(self.num1, self.num2)
            print(subtraido)
        
        elif self.operacao == 3:
            if self.num2 == 0:
                print('Você não pode dividir por 0!')
            else: 
                dividido = operacoes.divisao.div(self.num1, self.num2)
                print(dividido)

        elif self.operacao == 4:
            multiplicado = operacoes.multiplicacao.mult(self.num1, self.num2)
            print(multiplicado)
        
    
    def solicitar_info(self):
        self.operacao = int(input('Por favor, me forneça qual operação deseja realizar: '))
        self.num1 = int(input('Agora, me forneça o primeiro número que deseja operar: '))
        self.num2 = int(input('Agora, me forneça o segundo número que deseja operar: '))

    
    def exibir_instrucao(self):
        print('Olá, seja bem vindo à calculadora!')
        print('-----------------------------')
        print('Você tem as seguintes opções: \n 1 - somar \n 2 -subtrair \n 3 - dividir \n 4 - multiplicar')
