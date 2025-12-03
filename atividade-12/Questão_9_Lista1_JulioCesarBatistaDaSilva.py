#UFCA
#Fundamentos de Estrutura de Dados e Estruturas Lineares - 2° semestre
#Júlio Cesar Batista da Silva

#9. Crie um dicionário para armazenar os dados da tabela ante rior.
# Em seguida, o programa deve imprimir uma listagem de mulheres do setor de TI que recebem acima de R$ 3.000,00.

class Funcionarios:
    def __init__(self):
        self._dados = {}

    @property
    def dados(self):
        return self._dados

    @dados.setter
    def dados(self, valor):
        self.__verificarDicionario(valor)
        self._dados = valor

    def cadastrarFuncionario(self, nome: str, sexo: str, setor: str, salario: float | int):
        self.__verificarString(nome)
        self.__verificarString(sexo)
        self.__verificarString(setor)
        self.__verificarSalario(salario)

        self._dados[nome] = {
            "sexo": sexo.upper(),
            "setor": setor.upper(),
            "salario": salario
        }

    def listarMulheresTI(self):
        resultado = ""

        for nome, info in self._dados.items():
            if info["sexo"] == "F" and info["setor"] == "TI" and info["salario"] > 3000:
                resultado += f"{nome} — R$ {info['salario']}\n"

        if resultado == "":
            return "Nenhuma mulher do setor de TI recebe acima de R$ 3.000,00."

        return resultado

    def __str__(self):
        saida = ""
        for nome, info in self._dados.items():
            saida += f"{nome} | Sexo: {info['sexo']} | Setor: {info['setor']} | Salário: R$ {info['salario']}\n"
        return saida

    # Helpers
    def __verificarDicionario(self, valor):
        if not isinstance(valor, dict):
            raise ValueError("Os dados devem ser armazenados em um dicionário.")

    def __verificarString(self, texto):
        if not isinstance(texto, str) or texto.strip() == "":
            raise ValueError("O valor fornecido deve ser uma string válida.")

    def __verificarSalario(self, salario):
        if not isinstance(salario, (int, float)) or salario <= 0:
            raise ValueError("O salário deve ser um número maior que zero.")

func = Funcionarios()

func.cadastrarFuncionario("Ana Silva", "F", "TI", 4500)
func.cadastrarFuncionario("Mariana Souza", "F", "RH", 3800)
func.cadastrarFuncionario("Clara Rocha", "F", "TI", 2500)
func.cadastrarFuncionario("João Pereira", "M", "TI", 5000)

print(func.listarMulheresTI())
