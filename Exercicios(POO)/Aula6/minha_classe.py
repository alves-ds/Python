# As vezes, pode ser interessante criarmos classes com métodos estáticos, isto é, que não pertencem ao contexto do objeto nem da classe em si, não podendo assim ser modificados, mas podendo ser acessados diretamente por meio da classe. Vejamos um exemplo abaixo, criando uma classe para exibir erros:

class Error:

    @staticmethod
    def error_500():
        print('Internal Server Error')

    @staticmethod
    def error_404():
        print('Not Found')


Error.error_404()
Error.error_500()