'''Desenvolva um programa utilizando o para que faça a tabuada de um número
inteiro que será digitado pelo usuário. Mas a tabuada não deve necessariamente
iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados pelo
usuário.
Segue um exemplo: Montar a tabuada do: 5
Começar por: 4
Terminar em: 7
Saída de dados:
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35'''

n = int(input("Montar a tabuada do número: "))
inicio = int(input("Começar por:"))
fim = int(input("Terminar por:"))

for i in range(inicio,fim+1):
    print(f"{n} x {i} = {n*i}")

