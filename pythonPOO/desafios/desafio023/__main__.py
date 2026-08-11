from poligno import *
from rich import print, inspect

def main():
    q = Quadrado(20)
    # inspect(q, methods=True)
    print(f"O quadrado de lado {q.lado} tem perímetro de {q.perimetro():.1f}cm")
    print(f"O quadrado de lado {q.lado} tem área de {q.area():.1f}cm²")

    c = Circulo(12)
    # inspect(c, methods=True)
    print(f"O círculo de raio {c.raio} tem perímetro de {c.perimetro():.1f}cm")
    print(f"O círculo de raio {c.raio} tem área de {c.area():.1f}cm²")

if __name__ == "__main__":
    main()