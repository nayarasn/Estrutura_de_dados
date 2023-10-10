# 3. Crie uma função que verifica se uma palavra ou frase é um palíndromo 
# (lê-se igual de trás para frente, desconsiderando espaços e pontuação)

frase = (input("Olá, digite uma palavra ou uma frase para verificar se é um palíndromo: ")).strip().upper()
print()

def eh_palindromo(frase):
    # Remover espaços e pontuações e converter para minúsculas
    frase = ''.join(e for e in frase if e.isalnum()).lower()
    # Verificar se a frase é igual à sua inversa
    return frase == frase[::-1]

frase = "Hannah"  # Exemplo de palíndromo
resultado = eh_palindromo(frase)
print(f"A palavra ou frase: '{frase}' {'é' if resultado else 'não é'} um palíndromo.")