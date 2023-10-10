# 8. Faça um programa que determine se um número é primo ou não

numero = float(input("Olá, digite um número para saber se ele é primo ou não: "))
numero = int(numero)
print()

if numero <= 1:
    print(f"O número {numero} não é válido, pois não corresponde ao conjuto de números primos, tente novamente!")
else:
    divisores = 0
    # incrementa os divisores do número digitado
    for i in range(2, numero):
        if (numero % i) == 0:
            divisores += 1

# testa se a lista está vazia
if divisores == 0:
    print(f"O número {numero} é primo")
else:
     print(f"O número {numero} não é primo")


