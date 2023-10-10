# 1. Escreva um programa que recebe cinco notas de um aluno e calcula a média
# Em seguida, exiba se o aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7)

print("Olá, vamos calcular a média do seu aluno!")
print()

nota_1 = float(input("Digite a primeira nota do aluno: "))
nota_2 = float(input("Digite a segunda nota do aluno: "))
nota_3 = float(input("Digite a terceira nota do aluno: "))
nota_4 = float(input("Digite a quarta nota do aluno: "))
nota_5 = float(input("Digite a quinta nota do aluno: "))
print()

media = (nota_1 + nota_2 + nota_3 + nota_4 + nota_5) / 5

if media >= 7:
    print(f"A média do aluno foi {media:.2f} e ele está aprovado!")
else:
    print(f"A média do aluno foi {media:.2f} e ele está reprovado!")