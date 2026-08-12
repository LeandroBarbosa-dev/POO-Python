from abc import ABC, abstractmethod

class Trasnporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        # self.frete = frete

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Trasnporte):
    fator = 0.50

    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        frete = self.distancia * Moto.fator
        return frete


class Caminhao(Trasnporte):
    fator = 1.20
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia > 50:
            frete = self.distancia * Caminhao.fator
            return  frete
        else:
            return f"\nO frete para caminhão somente acima de 50 km"


class Drone(Trasnporte):
    fator = 9.50
    def __init__(self, distancia):
        super().__init__(distancia)

    def calc_frete(self):
        if self.distancia < 10:
            frete = self.distancia * Drone.fator
            return frete
        else:
            return f"\nO frete de drone somente distâncias menores que 10 km"
