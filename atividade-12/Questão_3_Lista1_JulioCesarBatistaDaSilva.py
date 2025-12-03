#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#3. Construa um programa que cadastre diversos voos aéreos, bem como sua origem e seu destino.
# Considere o número do voo como sendo a chave.
# Com base no que foi armazenado no dicionário, o programa deve informar a quantidade de voos cuja origem é Natal.

class Voos:
    def __init__(self):
        self._voos = {}

    @property
    def voos(self):
        return self._voos

    @voos.setter
    def voos(self, valor):
        self.__verificarValores(valor)
        self._voos = valor

    def cadastrarVoo(self, numeroVoo: int, origem: str, destino: str):
        self.__verificarNumeroVoo(numeroVoo)
        self.__verificarString(origem)
        self.__verificarString(destino)

        self._voos[numeroVoo] = {
            "origem": origem,
            "destino": destino
        }

    def quantidadeVoosOrigemNatal(self):
        contador = 0
        for numero, dados in self._voos.items():
            if dados["origem"].lower() == "natal":
                contador += 1
        return contador

    def __str__(self):
        saida = ""
        for numero, dados in self._voos.items():
            saida += f"Voo {numero}: {dados['origem']} → {dados['destino']}\n"
        return saida

    # Helpers
    def __verificarValores(self, valor):
        if not isinstance(valor, dict):
            raise ValueError("Os voos devem ser armazenados em um dicionário.")

    def __verificarNumeroVoo(self, numero):
        if not isinstance(numero, int):
            raise ValueError("O número do voo deve ser um número inteiro.")

    def __verificarString(self, texto):
        if not isinstance(texto, str) or texto.strip() == "":
            raise ValueError("O valor fornecido deve ser uma string válida.")


voos = Voos()

voos.cadastrarVoo(101, "Natal", "São Paulo")
voos.cadastrarVoo(202, "Rio de Janeiro", "Natal")
voos.cadastrarVoo(303, "Natal", "Recife")
voos.cadastrarVoo(404, "Brasília", "Curitiba")

print(voos)

print("Quantidade de voos com origem Natal:", voos.quantidadeVoosOrigemNatal())
