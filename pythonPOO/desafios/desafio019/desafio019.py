from rich import print
from time import sleep

class Livro:
    def __init__(self, titulo, paginas):
        self.titulo = titulo
        self.total_paginas = paginas
        self.pagina_atual = 1

        print(f":open_book: [blue]Você acabou de abrir o livro [green]'{self.titulo}'[/] que tem o total de {self.total_paginas} páginas. \nE você está na [yellow]páginas {self.pagina_atual}[/][/]")

    def passa_pagina(self,qtde = 1):
        cont = 0
        for pg in range(0, qtde, 1):
            if not self.fim_do_livro():
                self.pagina_atual += 1
                print(f"Pág {self.pagina_atual} :arrow_forward: ", end='')
                sleep(0.3)
                cont += 1
        print(f"[blue]Você avanço {cont} páginas e agora está na [/][yellow]página {self.pagina_atual}[/]")
        if self.fim_do_livro():
            print(f":closed_book: [red]Você chegou ao final do Livro '{self.titulo}'")

    def fim_do_livro(self):
        if self.pagina_atual == self.total_paginas:
            return True
        else:
            return False

l1 = Livro("O Poder do Agora", 20)
l1.passa_pagina(5)
l1.passa_pagina(10)
l1.passa_pagina(50)
