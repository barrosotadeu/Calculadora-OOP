from sys import exit
from math import sqrt, pow


class Calculadora:
    def __init__(self):
        pass

    def pegaNum(self):
        x = int(input("Informe o primeiro número:"))
        y = int(input("Informe o segundo número: "))
        return x, y

    def pegaNumPotRaiz(Self):
        x = int(input("Informe o número:"))
        y = int(input("Informe o grau da potenciação/raiz: "))
        return x, y    

    def soma(self):
        x, y = self.pegaNum()
        return x + y

    def sub(self):
        x, y = self.pegaNum()
        return x - y    

    def mul(self):
        x, y = self.pegaNum()
        return x * y

    def div(self):
        x, y = self.pegaNum()        
        return x / y

    def pot(self):
        x, y = self.pegaNumPotRaiz() 
        return pow(x, y)   

    def raiz(self):
        x, y = self.pegaNumPotRaiz()
        return pow(x, 1/y)    

    def sai(self):
        print("Saindo")
        return exit()   

    def erro(self):
        return "Opção inválida"

    def resultado(self, escolha):
        switcher = {
            1: self.soma,
            2: self.sub,
            3: self.mul,
            4: self.div,
            5: self.pot,
            6: self.raiz,
            7: self.sai

        }

        resultado = switcher.get(escolha, self.erro)()
        print(resultado)    
