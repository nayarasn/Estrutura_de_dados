# 5. Faça um programa que leia uma lista de números e retorne a média dos números pares

lista = [5, 1, 10, 16, 50, 2, 25]
dividendo = 0
divisor = 0

for i in lista:
    if (i % 2) == 0:
        dividendo += i
        divisor += 1

media_pares = dividendo / divisor

print(f"A lista é composta pelos seguintes números: {lista} | E a média dos pares é {media_pares:.2f}")