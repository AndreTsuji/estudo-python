# Ex 3 Controle televisao-----------------------------------
from unicodedata import name
from pip import main


class Televisao:
    def __init__(self) -> None:
        self.ligada = False
        self.canal = 5
        pass

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self):
        if self.ligada:
            self.canal += 1

    def diminui_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__': # Não executa trecho se o módulo for importado. Bom para trechos de teste.
    televisao = Televisao()
    print('Televisão está ligada? {}.'.format(televisao.ligada))
    televisao.power()
    print('Televisão está ligada? {}.'.format(televisao.ligada))
    print('Canal da televisao: {}.'.format(televisao.canal))
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print('Canal da televisao: {}.'.format(televisao.canal))
    televisao.diminui_canal()
    print('Canal da televisao: {}.'.format(televisao.canal))
