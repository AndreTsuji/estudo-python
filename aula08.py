from aula07_televisao import Televisao
from aula07_calculadora import Calculadora

televisao = Televisao()
print(televisao.ligada)
televisao.power()
print(televisao.ligada)

calc = Calculadora(5, 10)
print(calc.soma())
