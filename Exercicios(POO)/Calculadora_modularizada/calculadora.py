import operacoes

class Calculadora:

    def __init__(self, operacao: int, num1: int, num2: int) -> None:
        self.operacao = operacao
        self.num1 = num1
        self.num2 = num2


    def verificar_op(self):
        if self.operacao == 1:
            self.somar()
        
        elif self.operacao == 2:
            self.subtrair()
        

    def somar(self):
        soma1 = operacoes.soma.somar(self.num1, self.num2)
        return soma1

    def subtrair(self):
        subtracao = operacoes.subtracao.sub(self.num1, self.num2)
        return subtracao
    
    def dividir(self):
        divisao = operacoes.divisao.div(self.num1, self.num2)
        return divisao
    
    def multiplicar(self):
        multiplicacao = operacoes.multiplicacao.mult(self.num1, self.num2)
        return multiplicacao