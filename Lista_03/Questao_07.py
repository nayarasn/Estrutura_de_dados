# 7. Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura e peso

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("seu peso: "))
altura = float(input("sua altura: "))

resultado = calcular_imc(peso, altura)

print(f"Seu IMC é {resultado:.1f}")