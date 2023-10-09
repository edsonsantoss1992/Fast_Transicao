'''Desenvolva um programa que seja capaz de calcular a média
ponderada de um aluno. Inicialmente solicite o nome e as três notas
do aluno, logo após, calcule e exiba na tela a média. Na média
ponderada considere os seguintes pesos nas notas: 2, 3 e 5. Essa é a
fórmula para calcular a média.'''

nome= input("Qual o nome do aluno: ")
nota1= float(input("1° Nota: "))
nota2= float(input("2° Nota: "))
nota3= float(input("3° Nota: "))
media_ponderada=(nota1*2+nota2*3+nota3*5)/10
if media_ponderada>=7:
    print(f"Aprovado com media igual a {media_ponderada:.2f}")
elif media_ponderada>=5 and media_ponderada<=6.9:
    print(f"Recuperação com media igual a {media_ponderada:.2f}")
else:
    print(f"Reprovado com media igual a {media_ponderada:.2f}")
