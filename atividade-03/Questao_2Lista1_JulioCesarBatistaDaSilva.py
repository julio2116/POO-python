#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

def readValues():
    lista = []
    for i in range(10):
        inputNumber = int(input(f"informe o número {i + 1}:\n"))
        lista.append(inputNumber)

    ref = int(input("Informe um numero de referência:\n"))

    numerosMaiores = []
    numerosMenores = []
    refRepetida = 0

    for number in lista:
        if number > ref:
            numerosMaiores.append(number)
        if number < ref:
            numerosMenores.append(number)
        if number == ref:
            refRepetida += 1

    if len(numerosMaiores) > 0:
        print(f"Numeros MAIORES que o numero de referência {ref}:")
        for number in numerosMaiores:
            print(number)
    if len(numerosMenores) > 0:
        print(f"{len(numerosMenores)} numeros, são menores que o numero de referência {ref}:")
    if refRepetida > 0:
        print(f"O referência {ref}, se repete {refRepetida} vezes no vetor")
    

readValues()
