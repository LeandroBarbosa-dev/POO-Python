from rich import print, inspect
from rich.panel import Panel

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()


    def add_favoritos(self, nomeJogos):
        self.favoritos.append(nomeJogos)
        self.favoritos = sorted(self.favoritos)


    def ficha(self):
        titulo = f"Jogador <{self.nick}>"
        listaJogo = ""
        for jogo in self.favoritos:
            listaJogo += f":video_game: [blue]{jogo}[/]\n"
        conteudo = f"Nome real: [black on blue] {self.nome} [/]\n"
        conteudo += f"Jogos Favoritos:\n"
        conteudo += f"{listaJogo}"
        caixa = Panel(conteudo, title=titulo, width=40)
        print(caixa)

j1 = Gamer("Fabricio da Silva", "detonator2025")
# inspect(j1)
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olivia Souza", "peach_raivosa")
j2.add_favoritos("Mario Bros")
j2.add_favoritos("Call of Duty")
j2.ficha()