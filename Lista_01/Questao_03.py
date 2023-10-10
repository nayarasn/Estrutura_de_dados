# 3. Escreva um programa que solicite um número ao usuário e imprima todos os números pares de 0 até esse número

numero = float(input("Olá, digite um número para saber quem são os pares de 0 até ele: "))
numero = int(numero)
print()

if numero <= 0:
    print("Digite outro número acima de 0")
else:
    print(f"Os números pares de 0 até {numero} são:")
    for i in range(0, numero):
        if (i % 2) == 0:
            print(i)



