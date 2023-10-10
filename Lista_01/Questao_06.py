# 6. Escreva um programa que peça um número inteiro positivo ao usuário e calcule o fatorial desse número

numero = int(input("Olá, digite um número inteiro positivo para saber o seu fatorial: "))
print()

if numero < 0:
    print("O fatorial não contempla números negativos")
elif numero == 0:
    print("O fatorial de 0! é 1")
else:
    resultado = 1
    for i in range(1, numero + 1):
        # (numero + 1) para considerar o valor digitado
        resultado *= i
        # resultado = resultado * i --> resultado = 1 * 1 (para a primeira iteração)

print(f"O fatorial de {numero}! é igual a {resultado}")