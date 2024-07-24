"""
Faça um programa que represente um alistamento militar.
"""
from datetime import date

def menu_inicial():
  print("---------------------")
  print("BOAS VINDAS JOVEM!!!\nVOCÊ JÁ REALIZOU O ALISTAMENTO MILITAR?")
  print("--------------------")


def alistamento():
  menu_inicial()
  atual = date.today().year
  nasc = int(input("Qual o ano de nascimento: "))
  idade = atual - nasc
  print(f"Quem nasceu em {nasc} tem {idade} anos, ou irá fazer, em {atual}.")
  if idade == 18:
    print("Você deve se alistar")
    saldo = 18 - idade
  elif idade < 18:
    saldo = 18 - idade
    print(f"Ainda faltam {saldo} anos para alistamento")
  elif idade > 18:
    saldo = idade - 18
    print(f"Você já deveria ter se alistado há {saldo} anos, ou já prestou o serviço militar.")

alistamento()
