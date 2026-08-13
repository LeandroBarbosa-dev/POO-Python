from funcinarios import *
from rich import print, inspect


def main():

    f1 = Horista("José da Silva", 19.78, 220)
    f1.calc_sal()
    f1.analisar_sal()

    f2 = Mensalista("Maria de Souza", 8500)
    f2.calc_sal()
    f2.analisar_sal()


if __name__ == "__main__":
    main()