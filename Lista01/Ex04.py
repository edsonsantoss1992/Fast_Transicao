'''Desenvolva um programa para calcular a redução do tempo de vida
de um fumante. Pergunte a quantidade média de cigarros fumados
por dia e por quantos anos ele já fumou. Considere que um fumante
perde 10 min de vida a cada cigarro. Calcule e exiba quantos dias de
vida o fumante perdeu até o momento.'''

quant_media= int(input("Quantidade média de cigarros fumados por dia: "))
quant_anos= int(input("Quantidade de anos que já é fumante: "))
total_minutos_perdidos= (quant_media*10)*365*quant_anos
quant_dias_perdidos=total_minutos_perdidos/1440
print(f"Quantidade de dias perdidos = {quant_dias_perdidos:.2f}")
