'''Desenvolva uma função que permita receber uma variável
inteira X inúmeras vezes (deve parar quando o valor digitado for igual a
zero). Como retorno da função, para cada valor lido deverá ser imprimido a
sequência de 1 até X (o número digitado), com um espaço entre cada
número e seu sucessor.'''

def sucessores(num):
    for i in range(1,num+1):
        print(i,end=" ")

while True:
    numero= int(input("Digite um número: "))
    sucessores(numero)
    if numero==0:
        break
