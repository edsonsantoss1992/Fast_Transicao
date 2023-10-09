'''Um número é considerado triangular se ele é produto de três números naturais
consecutivos. Por exemplo: 120 é triangular, pois 4*5*6 = 120. O número 2730 é
triangular, pois 13*14*15 = 2730. Após o usuário digitar um número natural
(inteiro não-negativo), verifique se ele é triangular ou não.
'''

n = int(input("Qual o número que você deseja verificar: "))
i=1
while i * (i+1) * (i+2)<n:
    i+=1
if i * (i+1) * (i+2)==n:
    print(f"{n} é produto de {i}*{i+1}*{i+2}")
else:
    print("Não é produto.")


