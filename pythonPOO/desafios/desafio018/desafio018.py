from rich import print
from rich.panel import Panel

class Churrasco:
    # * Atributo de Classe:
    consumo_padrao = 0.4 #TODO: Cada pessoa com em média 400g de carne
    preco_kg = 82.40 #TODO: Cada Kg carne custo R$82.40

    def __init__(self, nome, qtidade):
        self.nome = nome
        self.qtidade = qtidade

    def __str__(self):
        return f'{self.nome} para {self.qtidade}'

    def calcular_qtd_carne(self):
        return Churrasco.consumo_padrao * self.qtidade

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * self.__class__.preco_kg
    
    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.qtidade

    def analisar(self):
        titulo = f'{self.nome}'
        conteudo = f'Analisando [cyan]{self.nome}[/] com [blue]{self.qtidade}[/] convidados.'
        conteudo += f'\nCada participante comerá 0.4kg e cada Kg custa R$82,40'
        conteudo += f'\nRecomendo [yellow]comprar {self.calcular_qtd_carne():.3f}Kg[/] de carne.'
        conteudo += f'\nO custo total será de [green]R${self.calcular_custo_total():,.2f}[/]'
        conteudo += f'\nCada pessoa pagará [magenta]R${self.calcular_custo_individual():,.2f}[/] para participar.'

        etiqueta = Panel(f'{conteudo}', title=titulo, width=70)
        return etiqueta

c1 = Churrasco('Churras dos Amigos', 15)
print(c1.analisar())

c2 = Churrasco('Festa do fim de ano', 80)
print(c2.analisar())