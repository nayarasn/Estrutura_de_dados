# 9. Escreva um programa que leia uma lista de nomes e retorne uma nova lista com apenas os nomes que começam com a letra 'A'

lista = ["Edilson", "Nayara", "Amora", "Alana", "Fatima", "Ambida"]

nomes_a = list(filter(lambda nome: nome.lower().startswith('a'), lista))

print("Nomes que começam com 'A':")
for nome in nomes_a:
    print(nome)