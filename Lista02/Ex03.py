'''A fabricação dos presentes para o Natal é um processo muito
complicado. Diversas vezes os duendes ficam até tarde trabalhando
para que tudo possa ser terminado a tempo e com perfeição. Para
melhor gerenciar seus cronogramas, os duendes estipularam quantos
minutos são necessários para fabricar cada presente.
Já está quase no final do expediente, e um dos duendes pediu sua
ajuda. Faltam N minutos para a hora de ir embora, e restam dois
presentes para o duende Ed fabricar. Solicite quantos minutos faltam, e
quanto tempo é necessário para fabricar cada um dos presentes.
Ajude-o a descobrir se conseguirá fabricar os dois ainda hoje, ou se
deve deixar para amanhã.'''

minutos_restantes= int(input("Quantos minutos faltam para o fim do expediente: "))
tempo= int(input("Quantos minutos são necessários para fabricar cada presente: "))
minutos_presente= minutos_restantes/2

if minutos_presente<tempo:
    print("Só será possível fabricar os dois presentes amanhã.")
else:
    print("Será possível fabricar todos os dois até o fim do expediente.")
