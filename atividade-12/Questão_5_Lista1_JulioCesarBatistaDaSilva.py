#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#5. Ainda com base no dicionário da questão 3, construa um pro grama em que, após os voos terem sido cadastrados,
# o usuário possa modificar a origem e/ou o destino de um determinado voo.
# Ao fim, o programa deve imprimir a nova listagem de voos.

class Voos:
    def __init__(self):
        self._voos = {}   # chave = número do voo / valor = {origem, destino}

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

    def alterarVoo(self, numeroVoo: int, novaOrigem: str = None, novoDestino: str = None):
        self.__verificarNumeroVoo(numeroVoo)

        if numeroVoo not in self._voos:
            raise ValueError("O voo informado não existe.")

        if novaOrigem is not None:
            self.__verificarString(novaOrigem)
            self._voos[numeroVoo]["origem"] = novaOrigem
        
        if novoDestino is not None:
            self.__verificarString(novoDestino)
            self._voos[numeroVoo]["destino"] = novoDestino

    def imprimirVoos(self):
        print(self)

    def __str__(self):
        saida = ""
        for numero, dados in self._voos.items():
            saida += f"Voo {numero}: {dados['origem']} → {dados['destino']}\n"
        return saida

    # -----------------------------
    # Helpers
    # -----------------------------
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

print("=== Voos cadastrados ===")
voos.imprimirVoos()

voos.alterarVoo(202, novaOrigem="Fortaleza")
voos.alterarVoo(303, novoDestino="Curitiba")

print("=== Nova listagem ===")
voos.imprimirVoos()
