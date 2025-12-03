#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#1. Um usuário do departamento de vendas de uma empresa necessita de um relatório que apresente seus clientes potenciais.
# Para isso, é necessário que o relatório seja ordenado do cliente que mais comprou para o que menos comprou.
# Os dados de entrada são razão social e valor total de compras.
# Considere a razão social como sendo a chave identificadora do cliente.

class RelatorioClientesPotenciais:
    def __init__(self):
        self._clientes = {}

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, valor):
        self.__verificarValores(valor)
        self._clientes = valor

    def adicionarCliente(self, razaoSocial: str, valorTotal: float):
        self.__verificarRazaoSocial(razaoSocial)
        self.__verificarValorCompra(valorTotal)

        self._clientes[razaoSocial] = valorTotal

    def gerarRelatorio(self):
        def chaveOrdenacao(item):
            return item[1]

        return sorted(
            self._clientes.items(),
            key=chaveOrdenacao,
            reverse=True
        )

    def imprimirRelatorio(self):
        for razao, valor in self.gerarRelatorio():
            print(f"Cliente: {razao} | Total Comprado: R$ {valor:.2f}")

    def __str__(self):
        saida = ""
        for razao, valor in self.gerarRelatorio():
            saida += f"{razao}: R$ {valor:.2f}\n"
        return saida

    # helpers
    def __verificarValores(self, valor):
        if not isinstance(valor, dict):
            raise ValueError("A lista de clientes deve ser um dicionário.")

    def __verificarRazaoSocial(self, razaoSocial):
        if not isinstance(razaoSocial, str) or razaoSocial.strip() == "":
            raise ValueError("A razão social deve ser uma string válida.")

    def __verificarValorCompra(self, valorTotal):
        if not isinstance(valorTotal, (int, float)):
            raise ValueError("O valor total deve ser numérico.")

relatorio = RelatorioClientesPotenciais()

relatorio.adicionarCliente("Alfa Ltda", 15000)
relatorio.adicionarCliente("Beta Comércio", 7000)
relatorio.adicionarCliente("Gamma Tech", 22000)

relatorio.imprimirRelatorio()

print("----\nComo texto da classe:\n")
print(relatorio)
