'''Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade
de números pares e a quantidade de números ímpares.'''

pares=0
impares=0
for i in range(5):
    n = int(input("Digite um número: "))
    if(n%2==0):
        pares+=1
    else:
        impares+=1
print(f"{pares} números pares.")
print(f"{impares} números impares.")
