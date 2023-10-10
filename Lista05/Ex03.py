'''Faça um programa que leia o nome do usuário e o imprima na vertical, em
forma de escada, usando apenas letras maiúsculas.'''

nome = input("Qual o nome do usuário: ").upper()
soma=''
for letra in nome:
    soma+=letra
    print(soma)
