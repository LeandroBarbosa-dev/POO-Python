from rich import print

class Caneta:
    def __init__(self, cor = "azul"):
        self.cor = cor
        self.escolha = ''
        self.caneta_tampada = True
        match cor:
            case "azul":
                self.escolha = "[blue]"
            case "vermelho" | "vermelha":
                self.escolha = "[red]"
            case "verde":
                self.escolha = "[green]"

    def escrever(self, msg):
        if self.caneta_tampada:
            print(f":prohibited: {self.escolha}A caneta da cor {self.cor} está tampada! ")
        else:
            print(f"{self.escolha}{msg}")

    def destampar(self):
        self.caneta_tampada = False

    def tampar(self):
        self.caneta_tampada = True

c1 = Caneta('azul')
c1.destampar()
c1.escrever("Funciona")

c2 = Caneta('vermelha')
c2.escrever("Teste de cor")

c3 = Caneta('verde')
c3.destampar()
c3.escrever("Estou testando minha classe")
c3.tampar()
c3.escrever("TESTE")

