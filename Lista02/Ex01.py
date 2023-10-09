'''Faça um algoritmo que leia a primeira letra do estado civil de uma
pessoa e mostre uma mensagem com a sua descrição (Solteiro, Casado,
Viúvo, Divorciado). Mostre uma mensagem de erro, caso a opção seja
inválida.'''

estado_civil= input("[S]-Solteiro\n"
                    "[C]-Casado\n"
                    "[V]-Viúvo\n"
                    "[D]=Divorciado\n"
                    "Qual o seu estado civil: ").upper()
if estado_civil=="S":
    print("Estado civil : Solteiro")
elif estado_civil=="C":
    print("Estado civil : Casado")
elif estado_civil=="V":
    print("Estado civil : Viúvo")
elif estado_civil=="D":
    print("Estado civil : Divorciado")
else:
    print("Opção inválida")
