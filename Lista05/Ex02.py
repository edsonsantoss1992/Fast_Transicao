'''Em um arquivo .txt existe uma quantidade de 10 valores que representam
medições de profundidade. Desenvolva um código que conte o número de vezes
que uma medição aumenta em relação à medição anterior. No exemplo abaixo, há
7 medições maiores que a anterior. Por exemplo.'''

arquivo=open("ex2.txt","w")
valores=[]
for v in range(10):
    valores.append(input("Digite a medição: "))
arquivo.writelines("\n".join(valores))
arquivo.close()

arquivo=open("ex2.txt","r")
c=0
for i, medida in enumerate(arquivo):
    medida=int(medida)
    if medida[i]!=medida[i+1]:
        c+=1
print(f"Quantidade de medições maiores que a anterior {c}")
