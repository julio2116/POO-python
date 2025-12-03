#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#7. Modifique o programa anterior de modo que o usuário informe o nome de uma série e o novo programa indique os nomes dos atores principais.
# Caso a série não esteja cadastrada, o pro grama deve informar isso ao usuário.

class Series:
    def __init__(self):
        self._series = {}

    @property
    def series(self):
        return self._series

    @series.setter
    def series(self, valor):
        self.__verificarDicionario(valor)
        self._series = valor

    def cadastrarSerie(self, nome: str, atoresPrincipais: list):
        self.__verificarString(nome)
        self.__verificarListaStrings(atoresPrincipais)

        self._series[nome] = atoresPrincipais

    def buscarAtores(self, nome: str):
        self.__verificarString(nome)

        if nome not in self._series:
            return f"A série '{nome}' não está cadastrada."

        atores = ", ".join(self._series[nome])
        return f"Atores principais de {nome}: {atores}"

    def __str__(self):
        saida = ""
        for nome, elenco in self._series.items():
            saida += f"Série: {nome}\nAtores principais: {', '.join(elenco)}\n\n"
        return saida

    # Helpers
    def __verificarDicionario(self, valor):
        if not isinstance(valor, dict):
            raise ValueError("As séries devem ser armazenadas em um dicionário.")

    def __verificarString(self, texto):
        if not isinstance(texto, str) or texto.strip() == "":
            raise ValueError("O valor fornecido deve ser uma string válida.")

    def __verificarListaStrings(self, lista):
        if not isinstance(lista, list) or len(lista) == 0:
            raise ValueError("A lista de atores deve conter pelo menos um nome.")
        for item in lista:
            if not isinstance(item, str) or item.strip() == "":
                raise ValueError("Todos os atores devem ser strings válidas.")


series = Series()

series.cadastrarSerie("Breaking Bad", ["Bryan Cranston", "Aaron Paul"])
series.cadastrarSerie("Stranger Things", ["Millie Bobby Brown", "David Harbour"])

print(series.buscarAtores("Breaking Bad"))
print(series.buscarAtores("The Office"))

