# 5. Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
# chamado “falar” que imprime uma mensagem com o nome da pessoa 

class Pessoa:

    def __init__(self, nome, idade, descircao):
        self.nome = nome
        self.idade = idade
        self.descricao = descircao

    def falar(self):
        print(f"A pessoa chamada {self.nome}, com {self.idade} anos, esta {self.descricao}")

pessoa = Pessoa ("Edilson", 26, "com uma beleza exuberante")
pessoa.falar()