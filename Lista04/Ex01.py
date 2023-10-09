'''Desenvolva um programa que possua dois vetores/listas (A e B) de 5
elementos cada (o usuário insere os valores nos dois vetores). Crie um
terceiro vetor (C) que seja a união entre os 2 vetores anteriores, ou seja,
que contém os números dos dois vetores. Após isso, apresente:
a) A soma dos números pares do vetor C;
b) A média dos números ímpares do vetor C;
c) O menor valor do vetor C.'''

vetor1=[]
vetor2=[]
pares=0
impares=0
soma= 0
pos=0
for i in range(3):
    vetor1.append(float(input("Digite um número [1]:")))
    vetor2.append(float(input("Digite um número [2]: ")))
vetor3=vetor1+vetor2
for i in vetor3:
    pos+=1
    if i%2==0:
        pares+=1
    else:
        impares+=1
        soma+=i
        media=soma/impares
    if pos==1:
        menor=i
    if i<menor:
        menor=i

print(f"Números pares {pares}")
print(f"média dos números impares {media:.2f}")
print(f"Menor número {menor}")
