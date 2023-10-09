'''Índice de Massa Corpórea (IMC) é um valor calculado baseado na
altura e no peso de uma pessoa. De acordo com o valor do IMC,
podemos classificar o indivíduo dentro de certas faixas:
Menor que 18.5: Abaixo do peso
Entre 18.5 e 24.9: Peso ideal
Entre 25 e 29.9: Sobrepeso
Entre 30 e 39.9: Obesidade
40 ou mais: Obesidade mórbida
Solicite a altura e o peso do usuário, calcule o seu IMC e mostre a
classificação. O IMC é calculado pela expressão peso/altura² (peso
dividido pelo quadrado da altura).'''

altura = float(input("Qual a altura: "))
peso = float(input("Qual o peso: "))
imc=peso/(altura*altura)

if imc<18.5:
    print(f"Abaixo do peso : imc={imc:.2f}")
elif imc>=18.5 and imc<=24.9:
    print(f"Peso ideal do peso : imc={imc:.2f}")
elif imc>=25 and imc<=29.9:
    print(f"Sobrepeso do peso : imc={imc:.2f}")
elif imc>=30 and imc<=39.9:
    print(f"Obesidade : imc={imc:.2f}")
else:
    print(f"Obesidade mórbida : imc={imc:.2f}")

