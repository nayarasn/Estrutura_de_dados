# 4. Escreva um programa que recebe um número inteiro positivo e calcula a soma de seus dígitos

numero = int(input("Digite um número inteiro: "))

# começa aqui

numero = int(input("Digite um número inteiro: "))
numeroString = str(numero)  
digitos = []

for digito_char in numeroString:
    digito = int(digito_char)
    digitos.append(digito)

soma = sum(digitos)

print("soma dos dígitos é:", soma)