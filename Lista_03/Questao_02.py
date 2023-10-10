# 2. Escreva uma função que calcula o fatorial de um número inteiro positivo fornecido pelo usuário

numero = int(input("Olá, digite um número inteiro positivo para saber o seu fatorial: "))
print()

def calcular_fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        # (numero + 1) para considerar o valor digitado
        resultado *= i
        # resultado = resultado * i --> resultado = 1 * 1 (para a primeira iteração)
    return resultado
    
resultado = calcular_fatorial(numero)

if numero < 0:
    print("O fatorial não contempla números negativos")
elif numero == 0:
    print("O fatorial de 0! é 1")
else:
    print(f"O fatorial de {numero}! é igual a {resultado}")