from terrenos.quadrado import TerrenoQuadrado
from terrenos.retangular import TerrenoRetangular
from engenheiro import Engenheiro

engenheiro = Engenheiro('João')
terrenoquadrado = TerrenoQuadrado(4)
terrenoretangular = TerrenoRetangular(2,3)

engenheiro.medir_perimetro(terrenoquadrado)
engenheiro.medir_perimetro(terrenoretangular)