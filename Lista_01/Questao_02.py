# 2. Crie um programa que determine se um número inserido pelo usuário é par ou ímpar

numero = float(input(" Olá, digite um número para saber se ele é par ou ímpar: "))
numero = int(numero)
print()

if numero % 2 == 0:
    print(f"Você informou o número {numero} e ele é par")
else:
    print(f"Você informou o número {numero} e ele é ímpar")