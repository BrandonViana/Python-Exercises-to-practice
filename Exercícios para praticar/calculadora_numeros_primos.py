'''
Escreva uma função que receba um número inteiro e retorne se ele é primo ou não
'''

def calculo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def calculadora_numeros_primos():
    numero = int(input("Digite um número inteiro: "))
    if calculo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

calculadora_numeros_primos()