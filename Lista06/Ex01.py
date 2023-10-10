'''Faça um programa que receba um valor em horas e dê duas opções ao
usuário, converter em minutos ou em segundos. A partir da escolha do
usuário, o programa deverá chamar a função específica de conversão. A
função para converter horas em minutos deverá receber como parâmetro a
hora e retornar o valor em minutos. A função para converter horas em
segundos deverá receber como parâmetro a hora e retornar o valor em
segundos. Por fim, o programa principal imprime o valor retornado pela
função.'''

def conversao_minutos(horas):
    conversao=horas*60
    return conversao
def conversao_segundos(minutos):
    conversao=minutos*3600
    return conversao
horas=int(input("Valor em horas para conversão: "))
op=int(input("1-Converter em minutos\n"
              "2-Converter em segundos\n"
              "Qual a opção: "))
minutos=conversao_minutos(horas)
segundos=conversao_segundos(horas)
if op==1:
    print(f"{horas} horas é igual a {minutos:.2f} minutos")
else:
    print(f"{horas} horas é igual a {segundos:.2f} segundos")
