# 10. Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o computador. O programa deve 
# solicitar a escolha do usuário e, em seguida, escolher aleatoriamente a escolha do computador e determinar o vencedor

import random

opcoes = ["Pedra", "Papel", "Tesoura"]

usuario = input("Escolha Pedra, Papel ou Tesoura: ").capitalize()
computador = random.choice(opcoes)

print(f"Computador escolheu: {computador}")

if (usuario, computador) in [("Pedra", "Tesoura"), ("Tesoura", "Papel"), ("Papel", "Pedra")]:
    resultado = "Usuário venceu!"
elif usuario == computador:
    resultado = "Empate!"
else:
    resultado = "Computador venceu!"

print(resultado)