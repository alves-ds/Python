# Exemplo de associação bilateral, quando as classes se reconhecem entre si. 

from modulos import Casa, Pessoa

casa_do_douglas = Casa()
Douglas = Pessoa('Douglas')

Douglas.set_local(casa_do_douglas)
casa_do_douglas.set_proprietario(Douglas)

proprietario = casa_do_douglas.get_proprietario()
proprietario.se_apresentar()

Douglas.apresentar_local()