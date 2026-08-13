from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel
# Para utilizar o Panel do rich precisa importar o print do rich.

class Funcionario(ABC):
    sal_minimo = 1612
    inss = 7.5

    def __init__(self, nome = None):
        self.nome = nome
        self.sal_bruto = 0
        self.salario = 0


    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        base = self.salario / Funcionario.sal_minimo
        titulo = "Analisando Salário"
        conteudo = f"O salário de [blue]{self.nome}[/] que é ([magenta]{self.__class__.__name__}[/]) é de [green]R${self.salario:.2f}[/] que corresponde a [yellow]{base:.1f} salários[/] minimos."
        caixa = Panel(conteudo, title= titulo, width=50)
        print(caixa)

class Horista(Funcionario):

    def __init__(self, nome, valor_hora = 7.37, qtde_horas = 220):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trab = qtde_horas
        self.sal_bruto = qtde_horas * valor_hora

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100 )
        return self.salario



class Mensalista(Funcionario):

    def __init__(self, nome, sal_bruto = Funcionario.sal_minimo):
        super().__init__(nome)
        self.sal_bruto = sal_bruto

    def calc_sal(self):
        self.salario = self.sal_bruto - (self.sal_bruto * Funcionario.inss / 100)


