#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#3. Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua cerimônia de formatura.
#Construa um programa para cadastrar os nomes das pessoas que compraram a rifa.
#Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome.
import random

class Rifa:
    def __init__(self, nomes: str | list[str]):
        self.nomes = nomes

    @property
    def nomes(self):
        return self._nomes
    
    @nomes.setter
    def nomes(self, valor = None):
        if(valor is None or not isinstance(valor, (str, list))):
            raise ValueError("Argumento precisa ser uma lista ou uma string")
        if(isinstance(valor, str)):
            self._nomes = list(valor)
            return
        self._nomes = valor

    def cadastrarNovo(self, valor = None):
        if(valor is None or not isinstance(valor, (str, list))):
            raise ValueError("Argumento precisa ser uma lista ou uma string")
        if(isinstance(valor, list)):
            for i in valor:
                if(not isinstance(i, str)):
                    raise ValueError("Todos os elementos devem ser do tipo string")
                
        if(isinstance(valor, list)):
            self._nomes += valor
            return
        self._nomes.append(valor)

    def sortear(self):
        aleatorio = random.randint(0, len(self._nomes) - 1)
        return self._nomes[aleatorio]
    
    def __str__(self):
        string = ""
        for i in self._nomes:
            string += f"{i}"
        return string

sorteio = Rifa(["Julio", "João"])

sorteio.cadastrarNovo("Pedro")
sorteio.cadastrarNovo(["João", "Maria"])

print(sorteio.sortear())