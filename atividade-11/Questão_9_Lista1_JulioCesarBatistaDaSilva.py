#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#9. Crie um programa que gere, aleatoriamente, uma matriz M.
# A quantidade de linhas e de colunas de M devem ser informa das pelo usuário.
# Ao fim, o programa de informar se M é uma matriz diagonal.

import random

class Matriz:
    def __init__(self, linhas: int, colunas: int):
        self.linhas = linhas
        self.colunas = colunas
        self._matriz = self.carregarMatriz(self._linhas, self._colunas)
    
    @property
    def linhas(self):
        return self._linhas
    
    @property
    def colunas(self):
        return self._colunas
    
    @linhas.setter
    def linhas(self, valor):
        self.__verificarValores(valor)
        self._linhas = valor

    @colunas.setter
    def colunas(self, valor):
        self.__verificarValores(valor)
        self._colunas = valor

    def EDiagonal(self):
        for j in range(0, len(self._matriz)):
            for i in range(0, j):
                if j == i:
                    continue
                if self._matriz[j][i] != 0:
                    return False
        return True
    
    def __str__(self):
        matriz = ""
        for i in self._matriz:
            matriz += f"{i}\n"
        return matriz
    
    #helpers
    def __verificarValores(self, valor = None):
        if(valor is None or not isinstance(valor, int)):
            raise ValueError("Ambos os argumentos devem ser numeros inteiros")
        
    def carregarMatriz(self, linhas, colunas):
        matrizLinhas = []
        for j in range(0, linhas):
            matrizColunas = []

            for i in range(0, colunas):
                matrizColunas.append(random.randint(0, 1))
            matrizLinhas.append(matrizColunas)

        return matrizLinhas
    
matriz = Matriz(2, 2)
print(matriz.EDiagonal())
print(matriz)