# 3. Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
# chamado “calcular_area” que retorna a área do retângulo

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = ()

    def calcular_area(self):
        self.area = (self.base * self.altura)
        return self.area

area = Retangulo(2, 3)
area.calcular_area()

print(f"A area do retangulo sera:{area.area:.2f} m²")

