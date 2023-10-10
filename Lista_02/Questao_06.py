# 6. Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade)

class Produto:

    def __init__(self, nome, preco, qtd):
        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def total(self):
        total = self.preco * self.qtd
        print(f"Valor total da mercadoria {self.nome} é de R${total}")

nomeProduto = input("Qual nome do produto? ")
preco = float(input("Qual o preço do produto? "))
qtd = int(input("Quantos produtos existem em estoque? "))

produto = Produto(nomeProduto, preco, qtd)
produto.total()
