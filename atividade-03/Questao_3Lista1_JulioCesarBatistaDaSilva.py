#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

import numpy as np

class Pilha:
    def __init__(self, limit: int = None):
        self.__verifyIntValue(limit, "Argumento de tamanho máximo da pilha é obrigatório")

        self.__limit = limit
        self.__lastIndex = -1
        self.__list = np.empty(self.__limit, dtype=int)


    def inserir(self, value: int = None):
        self.__verifyIntValue(value, "Insira um valor válido na pilha, tipo number")
        if self.__lastIndex == self.__limit - 1:
            raise ValueError("Pilha já alcançou o limite")
        else:
            self.__lastIndex += 1
            self.__list[self.__lastIndex] = value

    def getValue(self):
        if self.__lastIndex < 0:
            raise ValueError("Pilha está vazia")
        else:
            self.__lastIndex -= 1
            return self.__list[self.__lastIndex + 1]

    def peek(self):
        if self.__lastIndex < 0:
            raise ValueError("Pilha está vazia")
        else:
            print(self.__list[self.__lastIndex])

    def length(self):
        return self.__lastIndex + 1
        
    def __verifyIntValue(self, value: int = None, errorMessage: str = "Erro"):
        if value is None or not isinstance(value, int):
            raise ValueError(errorMessage)
        
def orderPilha(pilha: Pilha = None):
    if pilha is None or not isinstance(pilha, Pilha):
        raise ValueError("Função aceita apenas objetos do tipo pilha como argumento")
    if pilha.length() < 1:
        raise ValueError("A pilha está vazia")

    orderedPilha = []

    for i in range(pilha.length()):
        item = pilha.getValue()
        if len(orderedPilha) > 0:
            if orderedPilha[i - 1] > item:
                orderedPilha.append(orderedPilha[i - 1])
                orderedPilha[i - 1] = item
            else:
                orderedPilha.append(item)
        else:
            orderedPilha.append(item)

    for number in orderedPilha:
        print(number)
    

try:
    pilha = Pilha(3)
except ValueError as error:
    print(f"Erro: {error}")
except:
    print("Erro inesperado")
else:
    pilha.inserir(7)
    # pilha.peek()
    pilha.inserir(53)
    # pilha.peek()
    pilha.inserir(2)
    # pilha.peek()
    pilha.getValue()
    # pilha.peek()
    pilha.inserir(1)
    # pilha.peek()
    try:
        orderPilha(pilha)
    except ValueError as error:
        print(f"Erro: {error}")
    except:
        print("Erro inesperado")

