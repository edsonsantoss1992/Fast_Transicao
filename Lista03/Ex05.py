'''Crie um programa que leia vários números digitados pelo usuário e mostre no
final o somatório entre eles. Obs: O programa será interrompido quando o
número 1111 for digitado.'''

cont=0
soma=0
while True:
    n = int(input("Digite um número: "))
    if(n==1111):
        break
    else:
        cont+=1
        soma+=n
print(f"A soma de todos os números é {soma}")
