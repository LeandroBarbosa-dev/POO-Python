from transporte import *

def main():
    dist = 10

    frete = Drone(dist)

    print(f"O frete de {type(frete).__name__} vai custa = R${frete.calc_frete()}")

if __name__ == "__main__":
    main()