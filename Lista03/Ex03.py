'''Um petshop atende 5 cachorros por tarde. Faça um programa que solicite ao
usuário o código do serviço efetuado: (1 - banho; 2 - tosa; 3 - banho e tosa; 4-
outros). Por fim, exiba a quantidade de solicitações para cada um deles.'''

c1=0
c2=0
c3=0
c4=0
for i in range(5):
    print("1- banho")
    print("2- Tosa")
    print("3- banho e Tosa")
    print("4- Outros")
    op = int(input("Qual o código do serviço desejado: "))
    if(op==1):
        c1+=1
    elif(op==3):
        c2+=1
    elif(op==4):
        c3+=1
    else:
        c4+=1
print(f"{c1} banhos")
print(f"{c2} tosa")
print(f"{c3} banho e tosa")
print(f"{c4} outros")

