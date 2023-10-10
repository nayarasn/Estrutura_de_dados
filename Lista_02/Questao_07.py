# 7. Crie uma classe chamada “Carro” com atributos “marca”, “modelo” e “ano”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do carro

class Carro:

    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def info(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")

marca = input("Qual a marca do carro? ")
modelo = input("Qual o modelo do carro? ")
ano = int(input("Qual o ano do carro?  "))

meuCarro = Carro(marca, modelo, ano)
print("="*30)
meuCarro.info()
print("="*30)