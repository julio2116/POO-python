import numpy as np

class FilaCircular:
    def __init__(self, tamanhoVetor):                           #Cria a classe
        self.tamanhoVetor = tamanhoVetor                        #Define o tamanho do vetor no momento da instanciação
        self.inicio = 0                                         #Indice do valor atual
        self.final = -1                                         #Indice do ultimo elemento
        self.numero_de_elementos = 0                            #Quantidade de elementos
        self.valores = np.empty(self.tamanhoVetor, dtype=int)   #Criação da lista

    def __fila_vazia(self):                                     #Função auxiliar que verifica se a fila esta vazia
        return self.numero_de_elementos == 0
    
    def __fila_cheia(self):                                     #Função auxiliar que verifica se a fila esta cheia
        return self.numero_de_elementos == self.tamanhoVetor
    
    def enfileirar(self, valor):                                #Insere um novo item na fila
        if self.__fila_cheia():                                 #Verifica se a fila esta cheia para evitar erros e processamento desnecessario
            print('A fila está cheia')
            return
        if self.final == self.tamanhoVetor -1:                  #Se estiver no indice do ultimo elemento passa de volta ao primeiro elemento
            self.final = -1
        self.final += 1                                         #Se não estiver no ultimo avança o indice para o proximo elemento
        self.valores[self.final] = valor                        #Reatribui o valor a ser incluído na posição correta
        self.numero_de_elementos += 1                           #Adiciona um ao numero de elementos quando o novo valor for adicionado à fila

    def desenfileirar(self):                                    #Função para retirar o item da lista
        if self.__fila_vazia():                                 #Verifica se a fila está vazia para evitar erros e processamento desnecessário
            print('A fila está vazia')
            return

        temporaria = self.valores[self.inicio]                  #Armazena o valor removido temporariamente para retorna-lo posteriormente
        self.inicio += 1                                        #Avança para o próximo elemento da fila nas próximas execuções
        if self.inicio == self.tamanhoVetor:                    #Verifica se está no último elemento da lista
            self.inicio = 0                                     #Caso esteja no último elemento, retorna as execuções ao primeiro item
            self.numero_de_elementos -= 1                       #Reduz o numero de elementos
        return temporaria                                       #Retorna o elemento removido

    def primeiroFila(self):
        if self.__fila_vazia():
            return -1
        return self.valores[self.inicio]                        #Retorna o primeiro elemento da fila (O próximo a ser "trabalhado")

fila = FilaCircular(6)
fila.enfileirar(1)
fila.enfileirar(3)
print(fila.primeiroFila())
print(fila.desenfileirar())
fila.enfileirar(2)
print(fila.primeiroFila())
print(fila.desenfileirar())
print(fila.primeiroFila())