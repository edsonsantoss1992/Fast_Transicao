'''Foi realizada uma pesquisa de algumas características físicas de 5 alunos de um
curso, a qual coletou os seguintes dados referentes a cada pessoa para serem
analisados:
sexo (masculino e feminino)
cor dos olhos (azuis, verdes ou castanhos)
cor dos cabelos ( louros, castanhos, pretos)
idade
Faça um algoritmo que determine e escreva:
a) a quantidade de pessoas do sexo feminino cuja idade está entre 18 e 35;
b) a quantidade de pessoas que têm olhos castanhos e cabelos pretos.'''

cont1=0
cont2=0
for i in range(5):
    sexo = input("Qual o sexo (M/F): ").upper()
    cor = input("Cor dos olhos - (azuis/verdes/castanhos) :")
    cabelo = input("Cor dos cabelos - (Louros/Castanhos/Pretos) :")
    idade = int(input("Qual a idade: "))
    if sexo=="F" and 18<=idade<=35:
        cont1+=1
    if cor=="castanhos" and cabelo=="preto":
        cont2+=1
print(f"{cont1} a quantidade de pessoas do sexo feminino e com idade entre 18 e 35 anos.")
print(f"{cont2} a quantidade de pessoas com cabelos pretos e olhos castanhos")
