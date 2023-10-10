'''Sua organização acaba de contratar um estagiário para trabalhar no
Suporte de Informática, com a intenção de fazer um levantamento nas
sucatas encontradas nesta área. A primeira tarefa dele é testar todos os
mouses que se encontram lá, testando e anotando o estado de cada um
deles, para verificar o que se pode aproveitar.
Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber a quantidade de mouses, o
número de identificação e o tipo de defeito de cada um, sendo eles:
● necessita da esfera;
● necessita de limpeza;
● necessita troca do cabo ou conector;
● quebrado ou inutilizado'''

sucatas= {}
quant= int(input("Você deseja cadastrar quantos mouses: "))
total=0
esfera=0
limpeza=0
cabo=0
quebrado=0
for i in range(quant):
    id = int(input("Número de identificação: "))
    defeito=int(input("1- Necessita da esfera\n"
                      "2- Necessita de limpeza\n "
                      "3- Necessita de troca do cabo ou conector\n"
                      "4- Quebrado ou inutilizado \n"
                      "Qual a opção: "))
    total+=1
    if defeito==1:
        esfera+=1
    elif defeito==2:
        limpeza+=1
    elif defeito==3:
        cabo+=1
    else:
        quebrado+=1
    pct_esfera=(esfera/total)*100
    pct_limpeza=(limpeza/total)*100
    pct_cabo=(cabo/total)*100
    pct_quebrado=(quebrado/total)*100
lista= [pct_esfera,pct_limpeza,pct_cabo,pct_quebrado]
print(f"{'Situação' : <20} {'Quantidade' : >30} {'Percentual(%)' : >25}")
print(f"{'1-Necessita da esfera' : <20} {esfera:>25} {lista[0]: >25}")
print(f"{'2-Necessita de limpeza' : <20} {limpeza:>24} {lista[1]: >25}")
print(f"{'3-Necessita de troca de cabo ou conector':<20} {cabo:>6} {lista[2]: >25}")
print(f"{'4-Quebrado ou inutilizado' : <20} {quebrado: >21} {lista[3]: >25}")
