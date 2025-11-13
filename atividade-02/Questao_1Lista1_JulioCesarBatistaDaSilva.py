#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

import numpy as np

class VetorNaoOrdenado:                                             #Definição da classe usando a palavra reservada class
    def __init__(self, tamanhoVetor):                               #O método init é o construtor da classe, self é sempre o primeiro argumento dentro do métodos de uma classe, a palavra self é uma convenção, podendo assumir qualquer outro e se refere as variaveis internas de cada objeto não da classe, desta forma podem assumr valores diferente e isolados para instância da classe
        self.tamanhoVetor = tamanhoVetor                            #Criação de uma variavel de instância, que recebe o valor do parâmetro de mesmo nome
        self.ultimaPosicao = -1                                     #Criação de uma variavel de instância
        self.valores = np.empty(self.tamanhoVetor, dtype=int)       #Variavel de instância que recebe uma lista de tamanho "n" e valores vazios. O tamanho é definido com base no parâmetro passado no momento em que a classe é instanciada
    
    def imprimir(self):                                             #Aqui é definido um método que tem como objetivo imprimir todos os valores do array
        if self.ultimaPosicao == -1:                                #Inicio da estrutura if else, caso a condição seja satisfeita o código não executará o else, do contrário o primeiro bloco de código não será executado, uma vez que a variável referente ao tamnho do array inicia como -1, caso nenhum item tenha sido íncluído, ou todos os itens tenham sido removidos, o primeiro bloco é executado
            print('Vetor está vazio')
        else:
            for i in range(self.ultimaPosicao + 1):                 #A estrutura for in percorre um a um todos os itens de um array, a função "range" cria uma estrutura de 0 a até o valor numerico inteiro do parâmetro informado, sendo uma estrutura iterável por estruturas de repetição - Como o valor de ultimaPosicao se refere a posição dentro do array (de 0 a n), é necessário somar mais 1
                print(i, '-', self.valores[i])                      #A função print é executada ua vez para cada iteração, portanto cada item dentro do vetor
    
    def inserir(self, valor):
        if self.ultimaPosicao == self.tamanhoVetor - 1:             #Verifica se o tamnho do vetor é igual a última posição do vetor, pois a cada valor inserido o valor da varial última posição também aumenta
            print("Tamanho máximo do vetor foi atingido")
        else:
            self.ultimaPosicao += 1
            self.valores[self.ultimaPosicao] = valor                #Listas podem ser acessadas em posições especificas através do simbolo "[]" onde deve ser informado um numero interio que representa a posição do valor a ser acessado, aqui acessamos a últma posição (que representa o ultimo elemento válido dentro do vetor), e então inserimos o valor passado no parâmetro

    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao + 1):                     #itera sobre cada elemento do array e compara o valor atual com o valor recebido pelo parâmetro
            if valor == self.valores[i]:                            #Caso os valores sejam iguais retorna o valor de i usado para acessar a posição do array que deu match (indice do elemento)
                return i                                            #Encerra a função caso o valor esteja presente no array, caso hajam dois valores iguais será retornado o indice do primeiro valor
        return -1                                                   #Caso não encontre retorna -1 como um sinal de que o valor buscado não se encontra no array

    def excluir(self, valor):
        posicao = self.pesquisar(valor)                             #usamos o método interno "pesquisar" para obter o indice do valor alvo da exclusão
        if posicao == -1:                                           #Caso o retorno da função anterior seja -1 siginifica que o elemento não existe o vetor, portanto retornamos também -1
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):            #É feito um range que ao invés de partir de 0 parte parte do indice alvo da exclusão até o último indice do array
                self.valores[i] = self.valores[i + 1]               #Para simular uma exclusão é feita uma sobreposição dos valores a partir (e incluindo) do indice do elemento alvo da exclusão
            self.ultimaPosicao -= 1                                 #Como não é feita uma exclusão real, o último valor permanece no array porém ao reduzir o indice tornamos seu valor inacessivel ao usuáio
