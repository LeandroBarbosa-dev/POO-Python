from classes028 import Termostato
from rich import print

def main():
    t = Termostato()
    try:
        temp = float(input("Qual a temperatura desejada: "))
        t.temperatura = temp
    except Exception as e:
        print(f"[red]Houve um problema: {e}[/]")
    print(f"A temperatura atual é de: [blue]{t.ftemperatura}[/]")


if __name__ == "__main__":
    main()
