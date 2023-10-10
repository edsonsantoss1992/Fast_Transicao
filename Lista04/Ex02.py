'''Sua missão é auxiliar os atletas da School, escreva um programa que
receba o nome e o tempo (em minutos) de três voltas de 5 corredores e
armazene tais tempos em um dicionário, onde a chave é o nome do
corredor, e os valores são os minutos de cada volta. Por fim, deverá ser
mostrado a média (com três casas decimais) de tempo de cada corredor e
o nome todo em maiúsculo do corredor que obteve a menor média'''

atletas ={}
total= 0
for i in range(4):
    nome = input("Qual o nome: ")
    total-=total
    for j in range(3):
        minutos = int(input(f"Tempo em minutos da {j+1} volta: "))
        total+=minutos
        media=total/3
    atletas[nome]=media
menor_media=0
i=0
for nome,media in atletas.items():
    if i==0:
        menor_media=media
    if media<menor_media:
        menor_media=media
        nome=nome
    i+=1
print(f"O atleta {nome.upper()} possui a menor média igual a {menor_media}.")


