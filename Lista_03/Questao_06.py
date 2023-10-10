# 6. Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes nela

def conta_vogais(string):
    nome = string.lower()
    result = 0
    vogais = 'aeiou'
    for i in vogais:
        result += nome.count(i)
    return result

solicitado = input('informe a string ')
print(conta_vogais(solicitado))