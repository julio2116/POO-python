import classes

# questão 1
def testeQuestão1(nome= None, valor= None):
    try:
        ingresso = classes.Ingresso(nome, valor)
    except ValueError as error:
        print(f"Erro: {error}")
        print("Encerrando o programa...")
    except:
        print("Erro inesperado, encerrando o programa")
    else:
        ingresso.exibirValor()
        print(ingresso)

# testeQuestão1("Lola Palloza")
# testeQuestão1("Lola Palloza", "teste")
# testeQuestão1("Lola Palloza", 100)

# questão 2
def testeQuestao2(altura= None, largura= None):
    try:
        retangulo = classes.Retangulo(altura, largura)
    except ValueError as erro:
        print(f"Erro: {erro}")
        print("Encerrando programa")
    except:
        print("Erro inesperado")
        print("Encerrando o programa")
    else:
        retangulo.calcularPerimetro()
        retangulo.calcularArea()

# testeQuestao2("5.5", "3")
# testeQuestao2(5.5)
# testeQuestao2(5.5, 7)
# testeQuestao2(3, 2)


# questao 3
def testeQuestao3():
    listaDePontos = []
    def innerTeste(nome= None, x= None, y= None):
        try:
            ponto = classes.Ponto(nome, x, y)
        except ValueError as erro:
            print(f"Erro: {erro}")
            print("Este ponto não será incluído")
        except:
            print("Erro inesperado")
            print("Este ponto não será incluído")
        else:
            listaDePontos.append(ponto)
    
    innerTeste("teste")
    innerTeste("teste 2", 20, "5")
    innerTeste("teste 3", 20, 5)
    innerTeste("teste 4", 20, 50)
    innerTeste("teste 5", 200, 50)

    for item in listaDePontos:
        print(item)

testeQuestao3()