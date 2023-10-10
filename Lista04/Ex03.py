'''Leia a idade de 4 pessoas e armazene-as em uma lista. Após esta entrada
de dados, exiba:
i) As idades armazenadas;
ii) Média das idades;
iii) Maior e menor idade (pode usar max e min);'''


idades = []
for i in range(4):
    idades.append(int(input("Qual a idade: ")))
print(f"Idades armazenadas: {idades}")
print(f"Maior idade {max(idades)} e Menor idade {min(idades)}")
print(f"A média das idades: {sum(idades)/len(idades)}")

