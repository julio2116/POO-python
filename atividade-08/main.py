import numpy as np

class No:                                                       #Definição da classe No
    def __init__(self, valor):                                  #Construtor que recebe o valor do nó
        self.valor = valor                                      #Armazena o valor do no
        self.proximo = None                                     #Representa o "ponteiro" para o próximo elemento (Sendo None quando se fala do último nó)

    def mostrar_No(self):                                       #Mostra o nó
        print(self.valor)

class Lista_Encadeada:                                          #Lista que cria a relação entre os nós
    def __init__(self):
        self.primeiroLista = None                               #Armazena o endereço do nó criado anteriormente para posterior inserção do próximo nó inserido

    def inserir_Inicio(self, valor):                            #"Insere" um novo nó (nova ligação)
        novo = No(valor)                                        #Instanciação de um novo nó
        novo.proximo = self.primeiroLista                       #Liga o nó sendo inserido na cadeia, ao nó inserido anteriormente
        self.primeiroLista = novo                               #Atualiza o valor do endereço do nó anterior para o próximo nó a ser inserido

    def mostrar(self):                                          #Método para imprimir todos os nós
        atual = self.primeiroLista                              #Valor a ser printado na tela

        while atual is not None:                                #Caso o primeiro valor (última inserção) não seja None, continua no laço
            atual.mostrar_No()                                  #Mostra o valor atual do nó
            atual = atual.proximo                               #Atualiza o valor de atual para o próxim item na cadeia

    def excluir_inicio_lista(self):                             #Método de exclusão
        if self.primeiroLista.proximo is None:                  #Verifica se é o último item da lista
            print("Lista vazia")
            return None
        temporaria = self.primeiroLista                         #Armazena temporariamente o valor sendo excluido para retornar no fim da função
        self.primeiroLista = self.primeiroLista.proximo         #Faz com que o nó atual e anterior apontem para o mesmo nó que viria depois, criando uma ilusão de que o nó atual foi apagado
        return temporaria
    
    def pesquisar(self, valor):                                 
        if self.primeiroLista is None:                          #Verifica se a lista está vazia
            print('Lista vazia')
            return None
        atual = self.primeiroLista                              #Caso não esteja vazia assume o valor do primeiro item da lista para verificação
        while atual.valor != valor:                             #Enquanto não encontrar o valor buscado continua no loop
            if atual.proximo is None:                           #Quebra o loop caso o não haja um proximo nó
                return None
            else:                                               #Quebra o loop caso encontre o valor
                atual = atual.proximo

        return atual                                            #Retorna o valor buscado


lista = Lista_Encadeada()
lista.inserir_Inicio(12)
lista.inserir_Inicio(15)
lista.inserir_Inicio(18)
lista.mostrar()
lista.pesquisar()
lista.excluir_inicio_lista()

lista.inserir_Inicio(21)
lista.excluir_inicio_lista()
lista.excluir_inicio_lista()
lista.excluir_inicio_lista()
lista.mostrar()