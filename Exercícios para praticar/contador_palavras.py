# Escreva uma função que recebe uma string e retorna um dicionário com a contagem de cada palavra.

def contador_palavras():
    texto = input("Digite uma frase: ")
    palavras = texto.lower().split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.strip('.,!?') 
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem


print(contador_palavras())