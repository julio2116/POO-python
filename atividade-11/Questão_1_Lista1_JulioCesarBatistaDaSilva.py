#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#1. Um professor de Matemática deseja construir um programa para gerar uma Progressão Aritmética (PA). Para isso, devem ser informados 3 parâmetros de entrada:
# a) primeiro termo da PA
# b) quantidade de termos da PA e;
# c) razão dessa PA.
# Construa um programa para carregar e imprimir uma lista contendo os termos da PA, bem como a soma dos elementos da PA.
import numpy as np

class PA:
    def __init__(self, primeiro: int, qtd: int, razao:int):
        self.primeiro = primeiro
        self.qtd = qtd
        self.razao = razao
        self.lista = np.empty(self._qtd, dtype=int)
        self._pa = None
    
    @property
    def primeiro(self):
        return self._primeiro
    @property
    def qtd(self):
        return self._qtd
    @property
    def razao(self):
        return self._razao

    @primeiro.setter
    def primeiro(self, valor):
        self.__verificarValor(valor)
        self._primeiro = valor
    @qtd.setter
    def qtd(self, valor):
        self.__verificarValor(valor)
        self._qtd = valor

    @razao.setter
    def razao(self, valor):
        self.__verificarValor(valor)
        self._razao = valor

    def carregarPA(self):
        if(self._pa is not None):
            print("Lista já foi carregada")
            return
        
        list = []
        for i in range(0, self._qtd):
            list.append(self._primeiro + (i * self._razao))

        self._pa = list
        print("Lista carregada com sucesso")
    
        
    def __str__(self):
        self.__verificarLista()
        string = ""
        for i in self._pa:
            string += f"{i}, "

        return string[:-2]
    
    def somaElementos(self):
        self.__verificarLista()
        total = 0
        for i in self._pa:
            total += i
        return total
    
    #helpers

    def __verificarValor(self, valor: int = None):
        if(valor is None or not isinstance(valor, int)):
            raise ValueError("Primeiro termo deve ser um numero inteiro")
        
    def __verificarLista(self):
        if(self._pa is None):
            print("Lista não carregada")
            return


try:
    teste = PA(1, 5, 3)

    teste.carregarPA()
    print(teste)
    print(teste.somaElementos())

except ValueError as error:
    print(f"Erro: {error}")
except:
    print("Erro inesperado")