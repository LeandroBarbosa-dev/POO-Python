from rich import print
from rich import inspect

class Funcionario:
    empresa = 'Curso em Vídeo'

    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f':handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {Funcionario.empresa}.'

fun1 = Funcionario('Maria', 'Administração', 'Analista de RH')
# inspect(fun1, methods=True)
print(fun1.apresentacao())

# fun2 = Funcionario('Luiz', 'TI', 'Programador')
# print(fun2.apresentacao())

