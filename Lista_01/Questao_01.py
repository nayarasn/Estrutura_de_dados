# 1. Faça um programa que calcule a média de três números inseridos pelo usuário

print(" Olá, para calcular a média digite três números:")
print()

numero_1 = float(input("Digite o primeiro número: "))
numero_2 = float(input("Digite o segundo número: "))
numero_3 = float(input("Digite o terceiro número: "))

media = (numero_1 + numero_2 + numero_3) / 3

print(f"A média dos números informados é {media:.2f}")