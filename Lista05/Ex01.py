'''Faça um programa que peça ao usuário para inserir:
○ uma frase
○ uma palavra que está contida na frase
○ outra palavra que ele deseja substituir no lugar da primeira palavra inserida.
Por fim, o programa exibe a frase modificada, toda em letra maiúscula.'''

frase= input("Qual a frase: ")
palavra=input("Uma palavra que está na frase: ")
sub=input("Uma palavra pra substituir: ")
nova_frase=frase.replace(palavra,sub)
print(nova_frase.upper())
