from abc import ABC, abstractmethod

class IGatewayPagamento(ABC):
    @abstractmethod
    def cobrar(self, valor):
        pass

class GatewayCartao(IGatewayPagamento):
    def cobrar(self, valor):
        return f"Passsando o cartão no valor de: {valor}"

class GatewayPIX(IGatewayPagamento):
    def cobrar(self, valor):
        return f"Processando o PIX no valor de: {valor}"

class Pedido:
    def __init__(self, gateway: IGatewayPagamento):
        self.gateway = gateway

    def finalizar(self, valor):
        return self.gateway.cobrar(valor)

class GatewayTeste(IGatewayPagamento):
    def __init__(self):
        self.ultimo_valor = None

    def cobrar(self, valor):
        self.ultimo_valor = valor
        return f"TESTE_OK:{valor}"
    