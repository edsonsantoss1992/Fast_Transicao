'''Crie um programa que utilize o NumPy para realizar análises específicas sobre
as notas, como calcular a média das notas dos três primeiros alunos e verificar
quais alunos tiraram notas acima de 7.'''

import numpy as np

notas_alunos=np.array([[9,8,7],[10,6,8],[5,7.5,6.6],[10,10,9.5],[7.5,7.2,7]])
medias= []
for indice,notas in enumerate(notas_alunos[:3]):
    if indice==0:
        medias.append(sum(notas)/3)
    elif indice==1:
        medias.append(sum(notas)/3)
    else:
        medias.append(sum(notas)/3)

for indice,media in enumerate(medias):
    if media>=7:
        print(f"O {indice+1} aluno foi aprovado e teve media igual a {media:.2f}.")
    else:
        print(f"O {indice+1} aluno foi reprovado e teve media igual a {media:.2f}.")
