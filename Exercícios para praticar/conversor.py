"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão
"""


def menu_de_escolha():
  print("------------------------")
  print("Menu de opções: \n-1 Binário\n-2 Octadecimal\n-3 Hexadecimal")
  print("------------------------")

def conversor():
    numero = int(input("Digite um número inteiro para converter: "))
    menu_de_escolha()
    opcao = input(f"Qual conversor você escolhe para o número {numero}? ")
    binario = bin(numero)
    octa = oct(numero)
    hexadecimal = hex(numero)

    if opcao == "1":
      print(f"O numero {numero} convertido em binário, é: {binario[2::]}")
    elif opcao == "2":
      print(f"O numero {numero} convertido em Octadecimal, é: {octa[2::]}")
    elif opcao == "3":
      print(f"O numero {numero} convertido em Hexadecimal, é: {hexadecimal[2::]}")
    else:
      print("Opção inválida, tente novamente!!")

conversor()
