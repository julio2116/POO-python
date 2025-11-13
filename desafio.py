import numpy as np

class VetorNaoOrdenado:                                         #definição da classe usando a palavra reservada class
    def __init__(self, tamanhoVetor):                           #O método init é o construtor da classe, self é sempre o primeiro argumento dentro do métodos de uma classe, a palavra self é uma convenção, podendo assumir qualquer outro e se refere as variaveis internas de cada objeto não da classe, desta forma podem assumr valores diferente e isolados para instância da classe
        self.tamanhoVetor = tamanhoVetor                        #Criação de uma variavel de instância, que recebe o valor do parâmetro de mesmo nome
        self.ultimaPosicao = -1                                 #Criação de uma variavel de instância
        self.valores = np.empty(self.tamanhoVetor, dtype=int)   #Variavel de instância que recebe uma lista de tamanho "n" e valores vazios. O tamanho é definido com base no parâmetro passado no momento em que a classe é instanciada
    
    def imprimir(self):                                         #Aqui é definido um método que tem como objetivo imprimir todos os valores do array
        if self.ultimaPosicao == -1:                            #Inicio da estrutura if else, caso a condição seja satisfeita o código não executará o else, do contrário o primeiro bloco de código não será executado, uma vez que a variável referente ao tamnho do array inicia como -1, caso nenhum item tenha sido íncluído, ou todos os itens tenham sido removidos, o primeiro bloco é executado
            print('Vetor está vazio')
        else:
            for i in range(self.ultimaPosicao + 1):             #A estrutura for in percorre um a um todos os itens de um array, a função "range" cria uma estrutura de 0 a até o valor numerico inteiro do parâmetro informado, sendo uma estrutura iterável por estruturas de repetição - Como o valor de ultimaPosicao se refere a posição dentro do array (de 0 a n), é necessário somar mais 1
                print(i, '-', self.valores[i])                  #A função print é executada ua vez para cada iteração, portanto cada item dentro do vetor
    

vetor = VetorNaoOrdenado(5)
vetor.imprimir()
print(range(5))