'''Desenvolva um programa em Python que apure o resultado de uma votação para determinar o personagem favorito do desenho “The Simpsons”. Suponha que existam 2 candidatos cujos códigos são:

1 - Bart
2 - Homer
 
Considere que existe uma função que recebe e escreve em um arquivo .txt ou em uma lista/vetor os votos de 5 pessoas. Um voto é representado pelo código de identificação do candidato.

Na sequência, uma função para leitura deverá ser implementada, a qual deverá apresentar, como resultado:

o nome e a quantidade de votos do candidato mais votado
o nome e a quantidade de votos do menos votado
quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é um valor diferente de 1 e 2). '''

def votacao():
    total_votos= []
    total_bart= []
    total_homer= []
    total_nulo= []
    for i in range(10):
        voto= int(input("1- Bart\n"
                        "2- Homer\n"
                        "0- Nulo\n"
                        "Qual o seu personagem favorito: "))
        if voto==1:
            total_bart.append(voto)
        elif voto==2:
            total_homer.append(voto)
        else:
            total_nulo.append(voto)
    total_votos.append(total_bart)
    total_votos.append(total_homer)
    total_votos.append(total_nulo)
    return total_votos

def apuracao(total_votos):
    for pos,votos in enumerate(total_votos):
        if pos==0:
            total_bart=len(total_votos[pos])
        elif pos==1:
            total_homer=len(total_votos[pos])
        else:
            total_nulos=len(total_votos[pos])
    maior=total_bart
    menor= total_bart
    if total_bart!=total_homer:
        if total_homer>total_bart:
            maior=total_homer
            print(f"O personagem Homer foi o favorito com {total_homer} votos.")
        else:
            print(f"O personagem Bart foi o favorito com {total_bart} votos.")
        if total_homer<total_bart:
            menor=total_homer
            print(f"O personagem Homer foi o menos votado com {total_homer} votos.")
        else:
            print(f"O personagem Bart foi o menos votado {total_bart} votos.")
    else:
        print(f"Houve empate na votação ambos com {total_bart} votos.")
    print(f"O total de votos nulos foi igual a {total_nulos}.")


apuracao(votacao())

