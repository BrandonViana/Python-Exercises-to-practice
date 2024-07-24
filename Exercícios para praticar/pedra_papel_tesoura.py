"""
Crie um Programa que faça o computador jogar Jokenpô com você.
"""

from random import randint

def menu_inicial():
  print("~~~~~~~~~~~~~~~~~~~~~~")
  print("VAMOS JOGAR JOKENPÔ\n~~~~~~~~~~~~~~~~~~~~~~")
  print("VOU TE APRESENTAR AS OPÇÕES")
  print(" [0] PEDRA\n [1] PAPEL\n [2] TESOURA")
  print("~~~~~~~~~~~~~~~~~~~~~~")

def pedra_papel_tesoura():
  menu_inicial()
  itens = ("Pedra", "Papel", "Tesoura")
  computador = randint(0, 2)
  jogador = int(input("Qual sua jogada? "))
  print("-=" * 11)
  print(f"O computador escolheu {itens[computador]}")
  print(f"O Jogador escolheu {itens[jogador]}")
  print("-=" *11)
  jogadas(computador, jogador)

def jogadas(computador, jogador):
  if computador == 0: # Computador jogou pedra
    if jogador == 0:
      print("EMPATE")
    elif jogador == 1:
      print("JOGADOR VENCEU")
    elif jogador == 2:
      print("COMPUTADOR VENCEU")
    else:
      print("JOGADA INVÁLIDA")

  elif computador == 1: # Computador jogou papel
    if jogador == 0:
      print("COMPUTADOR VENCEU") 
    elif jogador == 1:
      print("EMPATE")
    elif jogador == 2:
      print("JOGADOR VENCEU")
    else:
      print("JOGADA INVÁLIDA")

  elif computador == 2: #Computador jogou tesoura
      if jogador == 0:
        print("JOGADOR VENCEU")
      elif jogador == 1:
        print("COMPUTADOR VENCEU")
      elif jogador == 2:
        print("EMPATE")
      else:
        print("JOGADA INVÁLIDA")

pedra_papel_tesoura() 