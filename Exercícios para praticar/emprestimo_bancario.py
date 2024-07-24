"""
Faça um programa para aprovar empréstimo bancário na compra de uma casa
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

"""
def menu():
    #Menu incial de boas vindas
    print("---------------------------")
    print("PROGRAMA DE EMPRÉSTIMO BANCÁRIO")
    print("---------------------------")

def emprestimo_bancario():
        menu()
        valor_casa = float(input("Digite o valor da casa: "))
        salario = float(input("Digite seu salário: "))
        anos_pag = int(input("Digite em quantos anos você deseja pagar a casa: "))
        prestacao_mensal = valor_casa / (anos_pag * 12)

        if prestacao_mensal < (0.3 * salario):
            print(f"Para pagar uma casa de R${valor_casa} em {anos_pag} anos, a prestação será de R${prestacao_mensal:.2f}\nPARABÉNS!!! VOCÊ CONSEGUIU O EMPRÉSTIMO!")
        else:
            print(f"Para pagar uma casa de R${valor_casa} em {anos_pag} anos, a prestação será de R${prestacao_mensal:.2f}\nEMPRÉSTIMO NEGADO!!")
            
emprestimo_bancario()