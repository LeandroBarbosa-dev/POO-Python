from abc import ABC, abstractmethod

class BebidaQuente(ABC):
    def preparar(self):
        print(f"---- Preparando Bebida ----")
        print(self.ferver_agua())
        print(self.misturar())
        print(self.servir())
        print(f"---- Bebida Pronta ----")
    
    def ferver_agua(self):
        return f"1. Fervendo água a 100 graus Celsius."

    @abstractmethod
    def misturar():
        pass

    @abstractmethod
    def servir():
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        return f"2. Passando água presurizada pelo pó de café moido."

    def servir(self):
        return f"3. Servindo em xícara pequena."


class Cha(BebidaQuente):
    def misturar(self):
        return f"2. Mergulhe o sachê de ervas na água."

    def servir(self):
        return f"3. Servindo em caneca com limão."


class Leite(BebidaQuente):
    def misturar(self):
        return f"2. Passando vapor presurizado para ferver o leite."

    def servir(self):
        return f"3. Servindo na caneca grande com café."

