# questão 1

class Ingresso:
    def __init__(self, nome: str = None, valor: float | int = None):
        if nome is None or valor is None:
            raise ValueError("Nome e valor devem ser informados")
        if not isinstance(nome, str) or not isinstance(valor, (float, int)):
            raise ValueError("Necessário que nome seja uma string e valor seja float ou int")
        
        self.nome = nome
        self.valor = valor

    def exibirValor(self):
        print(f"O valor do ingresso é: {self.valor}")

    def __str__(self):
        return f"O evento {self.nome}, custa {self.valor} reais, cada ingresso"
    

# questão 2

class Retangulo:
    def __init__(self, largura: float | int = None, altura: float | int = None):
        if largura is None or altura is None:
            raise ValueError("largura e altura devem ser informados")
        if not isinstance(largura, (float, int)) or not isinstance(altura, (float, int)):
            raise ValueError("Necessário que largura e altura sejam float ou int")
        
        self.largura = largura
        self.altura = altura

    def calcularPerimetro(self):
        perimetro = self.altura * 2 + self.largura * 2
        print(f"Perimetro = {perimetro}")

    def calcularArea(self):
        area = self.altura * self.largura
        print(f"Área = {area}")


# questão 3

class Ponto:
    def __init__(self, nome: str = None, x: int = None, y: int = None):
        if nome is None or x is None or y is None:
            raise ValueError("Informe valores para nome, x e y")
        if not isinstance(nome, str) or not isinstance(x, int) or not isinstance(y, int):
            raise ValueError("nome deve ser uma string e x e y devem ser inteiros")
        
        self.nome = nome
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"{self.nome}: ({self.x}, {self.y})"