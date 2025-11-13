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


class VetorOrdenado:
    def __init__(self, tamanhoVetor):
        self.tamanhoVetor = tamanhoVetor
        self.ultimaPosicao = -1
        self.valores = np.empty(self.tamanhoVetor, dtype=int)
    
    def imprimir(self):
        if self.ultimaPosicao == -1:
            print('Vetor está vazio')
        else:
            for i in range(self.ultimaPosicao + 1):
                print(i, '-', self.valores[i])

    def inserir(self, valor):
        if self.ultimaPosicao == self.tamanhoVetor - 1:             #Comparação para verificar se a aultima posição já foi atingida, caso sim, não executa o restante da lógica de inserção
            print("Tamanho máximo do vetor atingido")
            return                                                  #O uso de return é uma das formas de encerrar a chamada de uma função, interrompendo seu fluxo completo
        
        posicao = 0                                                 #Definição da variavel posição para uso fora do escopo da função for, onde seu valor é manipulado
        for i in range(self.ultimaPosicao + 1):                     #Range equivalente ao tamanho de valores válidos dentro do vetor
            posicao = i                                             #Posição assume o valor de i
            if self.valores[i] > valor:                             #Caso o valor atualmente verificado seja maior que o valor a ser inserido o laço é quebrado e sabemos que a posição correta a inserir o valor é i
                break
            if i == self.ultimaPosicao:                             #Se formos até o último valor sem encontrar um valor maior que o a ser inserido, este valor deve ficar na última posição de valores válidos i + 1
                posicao = i + 1

        y = self.ultimaPosicao
        while y >= posicao:                                         #y é um contador a ser decrementado, para não sobreescrever um valor que deveria ser acessado posteriormente para reposicionamento (assim perdendo seu valor), precisamos iniciar do final e decrementar de volta a posição onde o novo valor será inserido
            self.valores[y + 1] = self.valores[y]                   #Acessa a posição seguinte (y + 1) e atribui a ela a posição atual, desta forma a posição correta logo poderá ser sobreescrita sem riscos de perda a informação
            y -= 1                                                  #Decrementa y para acessar os valores mais antigos a cada iteração

        self.valores[posicao] = valor                               #Atribui na posição correta o valor reebido no parâmetro da função
        self.ultimaPosicao += 1                                     #Aumenta o limite de posições acessaveis no array
    
    def pesquisar(self, valor):
        for i in range(self.ultimaPosicao + 1):                     #Percorre todos os valores
            if self.valores[i] > valor:                             #Passa por qualquer valor abaixo do valor buscado, caso passe do valor buscado, significa que o valor não está no array
                return -1
            if self.valores[i] == valor:                            #Aqui o valor o valor é encontrado e o indice é devolvido
                return i
            if i == self.ultimaPosicao:                             #Neste caso o indice é igual a última posição, como passou pela verificação, de ser igual ao valor na última posição (portanto não é igual), o valor não está no array
                return -1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultimaPosicao):
                self.valores[i] = self.valores[i + 1]
            self.ultimaPosicao -= 1


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


pilha = Pilha(3)
pilha.desempilhar()
pilha.empilhar(10)
pilha.empilhar(20)
print(pilha.visualizar_topo())
pilha.empilhar(30)
print(pilha.visualizar_topo())
pilha.desempilhar()
print(pilha.visualizar_topo())
pilha.desempilhar()
print(pilha.visualizar_topo())