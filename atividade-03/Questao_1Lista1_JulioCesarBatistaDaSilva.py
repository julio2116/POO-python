#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

def orderVector(lista: list[int] = None, qtdEl: int = None):
    if lista is None or not isinstance(lista, list):
        raise ValueError("Primeiro argumento precisa ser do tipo lista")
    if len(lista) != qtdEl and qtdEl is not None:
        raise ValueError("Cumprimento da lista difere do valor passado como parâmetro")
    if qtdEl is None or not isinstance(qtdEl, int):
        qtdEl = len(lista)

    soma = 0
    for item in lista:
        if not isinstance(item, int):
            raise ValueError("Apenas valores numericos devem ser informados na lista")
        soma += item
    
    return print(soma / qtdEl)

def teste(lista, qtd = None):
    try:
        orderVector(lista, qtd)
    except ValueError as error:
        print(f"Error: {error}")
    except:
        print("Erro inesperado")

    
teste([0, 1, 3])
teste([])
teste([0, 1, 3], 6)
teste([0, 1, "a"], 3)
teste(7)
teste([0, 1, 5], 3)
teste("teste")