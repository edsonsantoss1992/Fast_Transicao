'''Desenvolva um programa em Python que apure o resultado de uma votação
para determinar o personagem favorito do desenho “The Simpsons”.
Suponha que existam 2 candidatos cujos códigos são:
1 - Bart
2 - Homer
Considere que existe uma função que recebe e escreve em um arquivo .txt ou em uma
lista/vetor os votos de 5 pessoas. Um voto é representado pelo código de
identificação do candidato.Na sequência, uma função para leitura deverá ser
implementada, a qual deverá apresentar, como resultado:
o nome e a quantidade de votos do candidato mais votado
o nome e a quantidade de votos do menos votado
quantidade de votos nulos (um voto nulo é um voto cujo código de identificação é
 um valor diferente de 1 e 2).'''
def votacao():
    arquivo=open("votacao.txt","w")
    voto = []
    for i in range(5):
        voto.append((input("1- Bart\n"
                        "2- Homer\n"
                        "0- Sair\n"
                        "Qual o seu personagem favorito: ")))

    for i in voto:
        arquivo.write(i+"\n")
    arquivo.close()

def apuracao(arquivo):
    total_bart=0
    total_homer=0
    total_nulos=0
    arq= open(arquivo,"r")
    for votos in arq:
        votos=int(votos)
        if votos==1:
            total_bart+=1
        elif votos==2:
            total_homer+=1
        else:
            total_nulos+=1
    if total_bart!=total_homer:
        if total_bart>total_homer:
            print(f"O vencedor foi o personagem Bart com {total_bart} votos.")
        else:
            print(f"O vencedor foi o personagem Homer com {total_homer} votos.")
    else:
        print(f"Houve empate na votação.")
    print(f"Total de votos nulos: `{total_nulos}")

votacao()
arquivo="votacao.txt"
apuracao(arquivo)
