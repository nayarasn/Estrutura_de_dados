# 2. Crie uma classe chamada “Livro” que tenha atributos “titulo” e “autor”. Implemente um método
# chamado “detalhes” que retorna uma string com as informações do livro

class Livro:

    def __init__(self, titulo, autor, descricao):
        self.titulo = titulo
        self.autor = autor
        self.descricao = descricao

    def detalhes(self):
        print(f"Autor: {self.autor}\nTítulo: {self.titulo}\ndescrição: {self.descricao}")

#titulo = input("Digite título do livro: ")
#autor = input("Digite o nome do autor: ")
#descricao = input("Apresente uma breve descrição do livro: ")

livro = Livro("Branca de neve","Não sei", "Filme de conto de fadas")
livro.detalhes()

