# 9. Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”
# Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo

class Triangulo:

    def __init__(self, lado1, lado2, lado3, perimetro):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.perimetro = perimetro

    def perimetr(self):
        perimetro = (self.lado1 + self.lado2 + self.lado3)
        print(f"O perimetro total do triagulo é de {perimetro}")


lado1 = float(input("Digite o lado 1: "))
lado2 = float(input("Digite o lado 2: "))
lado3 = float(input("Digite o lado 3: "))

triangulo = Triangulo(lado1, lado2, lado3, perimetro=2)
triangulo.perimetro()
