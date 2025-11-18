class Veiculo:
    def __init__(self, marca: str = None, modelo:str = None):
        self.marca = marca
        self.modelo = modelo

    @property
    def marca(self):
        return self.__marca
    @property
    def modelo(self):
        return self.__modelo

    @marca.setter
    def marca(self, marca: str = None):
        Veiculo.verificar_string(marca, "marca")
        self.__marca = marca

    @modelo.setter
    def modelo(self, modelo: str = None):
        Veiculo.verificar_string(modelo, "modelo")
        self.__modelo = modelo

    @staticmethod
    def verificar_string(objeto: str, tipo: str):
        if objeto is None or not isinstance(objeto, str) or len(objeto) < 1 or objeto.isspace():
            raise ValueError(f"Valor {tipo} inválido")
        
    def mover():
        print("Movendo")


class Carro(Veiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def mover(self):
        print(f"{self.marca} {self.modelo} está movendo na pista")

class Moto(Veiculo):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def mover(self):
        print(f"{self.marca} {self.modelo} está movendo na estrada")
    

moto = Moto(marca="Ford", modelo="teste")
carro = Carro(marca="teste", modelo="abc")
moto.mover()
carro.mover()

moto.marca = "teste"
carro.modelo = "teste"
moto.mover()
carro.mover()