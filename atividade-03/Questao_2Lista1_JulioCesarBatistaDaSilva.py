#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

def readValues():
    lista = []
    for i in range(10):
        inputNumber = int(input(f"informe o número {i}:\n"))
        lista.append(inputNumber)

    ref = int(input("Informe um numero de referência"))

    # if lista is None or ref is None:
    #     raise ValueError("Informe uma lista e uma referencia")
    # if not isinstance(lista, list) or not isinstance(ref, int):
    #     raise ValueError("A lista e a referencia tem de ser do tipo int")
    

def teste():
    try:
        readValues()
    except ValueError as error:
        print(f"Error: {error}")

teste()