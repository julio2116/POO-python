#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

import numpy as np

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
