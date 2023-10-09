'''Peça ao usuario que informe um número, logo após, calcula e exibe o fatorial do
número digitado. O fatorial de um número é calculado multiplicando todos os
valores inteiros entre o próprio número e 1.
Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120'''

n = int(input("Qual o número que você deseja ver o fatorial: "))
multi=1
for i in range(n,0,-1):
    multi=multi*i
print(f"O fatorial do número {multi}")
