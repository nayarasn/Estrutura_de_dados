# 1. Crie uma classe chamada “Circulo” que tenha um atributo “raio”
# Implemente um método chamado “calcular_area” que retorna a área do círculo

import math
class Circulo:

    def __init__(self, raio):
        self.raio = raio

#calcular_area
    def area(self):
        self.calcuar_area = (math.pi * self.raio**2)
        return self.calcuar_area

#Inserindo um raio qulquer de um circulo
area = Circulo(6)
print(f"A área do círculo é igual a {area.area():.2f} cm.")






