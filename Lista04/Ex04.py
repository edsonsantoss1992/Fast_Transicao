'''Desenvolva um programa no qual o usuário deverá inserir a
quantidade de pessoas que desejam realizar uma doação a um centro
de apoio no Recife. Depois, pergunte os nomes dos doadores e o
valor que deseja doar, respectivamente. No final imprima o
dicionário com o nome do doador (chave) e o valor inserido. Além
disso, exiba o total em doações arrecadado.'''

doadores = {}
quant = int(input("Quantas pessoas irão realizar a doação: "))
soma=0
for i in range(quant):
    nome = input("Qual o nome: ")
    valor = float(input("Quanto você deseja doar: "))
    doadores[nome]=valor
    soma+=doadores[nome]

for nome,valor in doadores.items():
    print(f"{nome} realizou uma doação de {valor:.2f} reais ")

print(f"O valor total arrecadado foi {soma:.2f}")
