#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#5. Crie um programa que declare uma lista L, a qual você pode preenchê-la manualmente.
# Em seguida, o programa deve calcular a média geométrica entre o menor e o maior elemento da lista L.
# Ao fim, o programa deve imprimir a média geométrica encontrada.

class MinhaLista:
    def __init__(self, lista: list[int]):
        self.lista = lista
    
    @property
    def lista(self):
        return self._lista
    
    @lista.setter
    def lista(self, valor = None):
        if(valor is None or not isinstance(valor, list)):
            raise ValueError("Forneça uma lista de valores")
        self._lista = valor

    def incluir(self, valor = None):
        if(valor is None or not isinstance(valor, (int, list))):
            raise ValueError("Argumento precisa ser uma lista ou um numero inteiro")
        if(isinstance(valor, list)):
            for i in valor:
                if(not isinstance(i, int)):
                    raise ValueError("Todos os elementos devem ser do tipo int")
            
        if(isinstance(valor, list)):
            self._lista += valor
            return
        self._lista.append(valor)

    def mediaGeometrica(self):
        maior = max(self._lista)
        menor = min(self._lista)
        mediaGeometrica = (maior * menor) ** (1/2)

        return mediaGeometrica
    
    def __str__(self):
        string = ""
        for i in self._lista:
            string += f"{i}, "
        return string[:-2]
    
lista = MinhaLista([1,5,7])

lista.incluir([9, 5])

print(lista)

print(lista.mediaGeometrica())