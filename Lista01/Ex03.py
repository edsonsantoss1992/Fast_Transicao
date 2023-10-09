'''Desenvolva um programa que receba o nome de um ciclista, a
distância que ele percorreu em Km e o tempo que ele gastou nesse
percurso, em horas. O programa deverá calcular a velocidade média
do ciclista e, exibi-la na tela duas vezes, uma em Km/h e a outra em
m/s. Dividimos por 3,6 quando queremos converter Km/h para m/s.'''

nome = input("Qual o nome do ciclista: ")
distancia= float(input("Qual a distância percorrida em km: "))
tempo = int(input("Qual o tempo gasto: "))
vel_media_km= distancia/tempo
vel_media_ms= vel_media_km/3.6
print(f"Velocidade média em km: {vel_media_km}")
print(f"Velocidade média em M/s: {vel_media_ms:.2f}")
