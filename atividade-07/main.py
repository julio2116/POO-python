# ======== ÁREA DO ALUNO ========
# Implemente aqui as classes solicitadas no enunciado
# Use os mesmos nomes de classes e métodos.

class Pessoa:
    def __init__(self, nome: str = None):
        self.nome = nome

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome:str = None):
        if nome is None or not isinstance(nome, str) or len(nome) < 1 or nome.isspace():
            raise ValueError("Informe um valor válido, apenas strings não vazias")
        self.__nome = nome

    def apresentar(self):
        print(f"Olá, eu sou {self.__nome}")

class Funcionario(Pessoa):
    def __init__(self, nome: str = None, salario: float|int = None):
        super().__init__(nome)
        self.salario = salario

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario: float|int = None):
        if salario is None or isinstance(salario, (float, int)) or salario <= 0:
            raise ValueError("Atributo salario deve ser do tipo int ou float e ter valor acima de 0")
        self.__salario = float(salario)

    def calcular_salario(self):
        return self.salario
    
    def apresentar(self):
        super().apresentar()
        print("Atualmente estou trabalhando")


class Estudante(Pessoa):
    def __init__(self, nome:str = None, curso:str = None, bolsa: float|int = None):
        super().__init__(nome)
        self.curso = curso
        self.bolsa = bolsa

    @property
    def curso(self):
        return self.__curso
    
    @property
    def bolsa(self):
        return self.__bolsa

    @curso.setter
    def curso(self, curso:str = None):
        if curso is None or not isinstance(curso, str) or len(curso) < 1 or curso.isspace():
            raise ValueError("Curso não pode estar vazio")
        self.__curso = curso
    
    @bolsa.setter
    def bolsa(self, bolsa: float|int = None):
        if bolsa is not None and (not isinstance(bolsa, (int, float)) or len(bolsa) < 1):
            raise("Bolsa deve ser um numero acima de 0")
        self.__bolsa = bolsa

    def calcular_bolsa(self):
        if self.__bolsa is not None:
            return self.__bolsa
        return f"O Aluno {self.nome} não possui bolsa"
    
    def apresentar(self):
        print(f"Meu nome é {self.nome} e sou estudante")


class Gerente(Funcionario):
    def __init__(self, nome, salario, equipe:list[Funcionario] = None):
        super().__init__(nome, salario)
        self.equipe = equipe

    @property
    def equipe(self):
        return self.__equipe
    
    @equipe.setter
    def equipe(self, equipe:list[Funcionario] = None):
        if equipe is not None and not isinstance(equipe, list):
            raise ValueError("Atributo equipe deve ser do tipo list de Funcionarios ou do tipo Funcionario")
        if equipe is not None and isinstance(equipe, list):
            for funcionario in equipe:
                if not isinstance(funcionario, Funcionario):
                    raise ValueError("Todos os funcionários devem ser do tipo Funcionario")
            self.__equipe = equipe
        
    def incluirFuncionario(self, funcionario: str = None):
        if funcionario is not None and isinstance(funcionario, Funcionario):
            self.__equipe.append(funcionario)

    def apresentar(self):
        return f"Olá sou o gerente da equipe"
    

class AssistentePesquisa(Estudante, Funcionario):
    def __init__(self, nome, curso, salario, bolsa):
        super().__init__(nome, curso, salario, bolsa)


# ======== ÁREA DO PROFESSOR — NÃO ALTERAR ========
# Orquestrador de testes para o VPL usando vpl_evaluate.cases

import io
import sys
import contextlib


def _safe_run(func, *args, **kwargs):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        try:
            ret = func(*args, **kwargs)
            return True, ret, buf.getvalue()
        except Exception as e:
            return False, e, buf.getvalue()


def _ok(cond, msg):
    if not cond:
        raise AssertionError(msg)


def _contains_any(text, kws):
    t = text.lower()
    return any(k.lower() in t for k in kws)


def _extract_text(ret, printed):
    if isinstance(ret, str) and ret.strip():
        return ret.strip()
    if printed.strip():
        return printed.strip()
    return ""


# Cada função cmd_* faz UM teste e imprime:
# - "OK" se passar
# - "FAIL: mensagem" se falhar

def cmd_exists():
    try:
        for name in ["Pessoa", "Funcionario", "Estudante", "Gerente", "AssistentePesquisa"]:
            _ok(hasattr(sys.modules[__name__], name), "Classe ausente: " + name)
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_inheritance():
    try:
        P = Pessoa
        F = Funcionario
        E = Estudante
        G = Gerente
        AP = AssistentePesquisa

        _ok(issubclass(F, P), "Funcionario deve herdar de Pessoa")
        _ok(issubclass(E, P), "Estudante deve herdar de Pessoa")
        _ok(issubclass(G, F), "Gerente deve herdar de Funcionario")
        _ok(issubclass(AP, E), "AssistentePesquisa deve herdar de Estudante")
        _ok(issubclass(AP, F), "AssistentePesquisa deve herdar de Funcionario")

        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_pessoa_apresentar():
    try:
        p = Pessoa("Ana")
        ok_ret, ret, printed = _safe_run(p.apresentar)
        t = _extract_text(ret, printed)
        _ok("ana" in t.lower(), "Pessoa.apresentar deve mencionar o nome")
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_func_apresentar():
    try:
        f = Funcionario("Joao", 5000)
        ok_ret, ret, printed = _safe_run(f.apresentar)
        t = _extract_text(ret, printed)
        _ok(_contains_any(t, ["funcion", "sal", "5000"]), "Funcionario.apresentar incompleto")
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_est_apresentar():
    try:
        e = Estudante("Maria", "Computacao", 900)
        ok_ret, ret, printed = _safe_run(e.apresentar)
        t = _extract_text(ret, printed)
        _ok(_contains_any(t, ["estud", "curso", "comput", "bolsa"]), "Estudante.apresentar incompleto")
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_gerente_apresentar():
    try:
        g = Gerente("Bia", 8000, ["Ana", "Pedro"])
        ok_ret, ret, printed = _safe_run(g.apresentar)
        t = _extract_text(ret, printed)
        _ok(_contains_any(t, ["equipe", "ana", "pedro", "2"]), "Gerente.apresentar incompleto")
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_assistente_mro():
    try:
        mro = [c.__name__ for c in AssistentePesquisa.mro()]
        _ok("Estudante" in mro, "MRO não contém Estudante")
        _ok("Funcionario" in mro, "MRO não contém Funcionario")
        _ok(mro.index("Estudante") < mro.index("Funcionario"),
            "Estudante deve vir antes de Funcionario no MRO")
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_assistente_apresentar():
    try:
        ap = AssistentePesquisa("Leo", "ADS", 3000, 500)
        ok_ret, ret, printed = _safe_run(ap.apresentar)
        t = _extract_text(ret, printed)
        _ok(_contains_any(t, ["estud", "ads", "curso"]),
            "AssistentePesquisa.apresentar não menciona Estudante")
        _ok(_contains_any(t, ["funcion", "sal", "3000"]),
            "AssistentePesquisa.apresentar não menciona salário")
        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_super_chain():
    try:
        ap = AssistentePesquisa("Joao", "Engenharia", 3500, 700)

        _ok(hasattr(ap, "nome"), "nome não inicializado")
        _ok(hasattr(ap, "curso"), "curso não inicializado")
        _ok(hasattr(ap, "salario"), "salario não inicializado")
        _ok(hasattr(ap, "bolsa"), "bolsa não inicializada")

        _ok(ap.nome == "Joao", "nome incorreto")
        _ok(ap.curso == "Engenharia", "curso incorreto")
        _ok(float(ap.salario) == 3500, "salario incorreto")
        _ok(float(ap.bolsa) == 700, "bolsa incorreta")

        print("OK")
    except Exception as e:
        print("FAIL:", e)


def cmd_calc_methods():
    try:
        f = Funcionario("Zoe", 6000)
        e = Estudante("Marcos", "SI", 550)

        ok_ret, ret, _ = _safe_run(f.calcular_salario)
        _ok(isinstance(ret, (int, float)) and float(ret) == 6000,
            "calcular_salario errado")

        ok_ret, ret, _ = _safe_run(e.calcular_bolsa)
        _ok(isinstance(ret, (int, float)) and float(ret) == 550,
            "calcular_bolsa errado")

        print("OK")
    except Exception as e:
        print("FAIL:", e)


CMDS = {
    "exists": cmd_exists,
    "inheritance": cmd_inheritance,
    "pessoa_apresentar": cmd_pessoa_apresentar,
    "func_apresentar": cmd_func_apresentar,
    "est_apresentar": cmd_est_apresentar,
    "gerente_apresentar": cmd_gerente_apresentar,
    "assist_mro": cmd_assistente_mro,
    "assist_apresentar": cmd_assistente_apresentar,
    "super_chain": cmd_super_chain,
    "calc_methods": cmd_calc_methods,
}

if __name__ == "__main__":
    comando = sys.stdin.read().strip()
    func = CMDS.get(comando)
    if func is None:
        print("FAIL: comando inválido:", comando)
    else:
        func()
