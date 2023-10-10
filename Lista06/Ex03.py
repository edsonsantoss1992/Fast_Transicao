'''Desenvolva um programa que tenha uma função chamada auxilio() que irá
receber como parâmetro o ano de nascimento de uma pessoa, retornando
como resultado se uma pessoa terá ou não direito ao auxilio escolar:
Autorizado: entre 4 (incluso) e 16 anos (incluso);
Negado: menos de 4 anos e maior que 16.'''

from datetime import date
def auxilio(ano):
    ano_atual=date.today().year
    idade=ano_atual-ano
    if(idade>=4 and idade<=16):
        print("Auxílio autorizado.")
    else:
        print("Auxílio negado")
ano=int(input("Qual o ano de nascimento: "))
auxilio(ano)
