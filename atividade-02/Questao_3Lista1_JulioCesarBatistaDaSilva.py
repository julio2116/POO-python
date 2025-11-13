#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

import numpy as np

class Pilha:                                                        #Definição da classe pilha
    def __init__(self, tamanhoPilha):
        self.__tamanhoPilha = tamanhoPilha                          #Recebimento do parâmetro tamanhoPilha para definir a mesma variavel interna
        self.__topo = -1                                            #Definição do "Tamanho", padrão para cada instância da Classe
        self.__valores = np.empty(self.__tamanhoPilha, dtype=int)   #Define um array vazio de n posições vazias tipadas em int, numeros inteiros

    def __pilha_cheia(self):
        # print(self.__tamanhoPilha, self.__topo)
        if self.__topo == self.__tamanhoPilha:                      #Retorna true se a pilha estiver cheia, conforme novos elementos forem incluidos "topo" será incrementado até ficar igual ao tamanho da pilha
            return True
        else:
            return False
        
    def __pilha_vazia(self):
        if self.__topo == -1:                                       #Se topo for igual a -1 a pilha está vazia, retornando true, topo será decrementado a cada valor excluido
            return True
        else:
            return False
        
    def empilhar(self, valor):                                      #Utiliza a função privada para verificar se a pilha está cheia, se sim retorna o erro
        if self.__pilha_cheia():
            print("Pilha está cheia")
        else:
            self.__topo += 1                                        #Amplia o tamanho de valores válidos na pilha 
            self.__valores[self.__topo] = valor                     #Reatribui o valor do array na posição do topo já incrementado
    
    def desempilhar(self):
        if self.__pilha_vazia():                                    #Utiliza a função privada para verificar se a pilha está vazia, se sim retorna o erro
            print("A pilha está vazia")
        else:
            self.__topo -= 1                                        #Reduz o tamanho da pilha para simular retirada do valor do topo, que poderá ser sobrescrito na função de empilhar

    def visualizar_topo(self):
        if self.__pilha_vazia():                                    #Aqui escolhi continuar utilizando a função de verificação de pilha vazia para evitar repetir o mesmo código novamente, mantendo o padrão de retornar o erro primeiro
            return -1
        else:
            return self.__valores[self.__topo]                      #Retorna o valor na posição n do último valor válido inserido na pilha
