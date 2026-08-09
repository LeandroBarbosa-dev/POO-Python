from rich import print
from rich.panel import Panel
from rich import inspect

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f'{self.nome} custa R${self.preco:,.2f}'

    def etiqueta(self):
        caixa = f'{self.nome.center(30, ' ')}'
        caixa += f'{'-' * 30}'
        precof = f'R${self.preco:,.2f}'
        caixa += f'{precof.center(30, '.')}'
        etiqueta = Panel(f'[white]{caixa}[/]', title='Produto', width=34, style='green')
        return etiqueta


prod1 = Produto('Iphone 17 Pro Max', 11500)
prod2 = Produto('Notebook Gamer', 8000)
# print(prod1)
print(prod1.etiqueta())
print(prod2.etiqueta())
