'''Escreva um programa que leia três valores com ponto flutuante: A, B e
C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem o valor de A como base e
o valor de C como altura.
b) a área do círculo que tem como raio o valor de C.
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem como lado o valor de B.
e) a área do retângulo que tem lados A e B.'''

a = float(input("Qual o valor de A: "))
b = float(input("Qual o valor de B: "))
c = float(input("Qual o valor de C: "))
pi=3.14
area_Triangulo=(a*c)/2
area_Circulo=pi*(c*c)
area_Trapezio=((a+b)*c)/2
area_Quadrado=b*b
area_Retangulo=a*b
print(f"Área triângulo = {area_Triangulo}")
print(f"Área Círculo = {area_Circulo}")
print(f"Área Trapézio = {area_Trapezio}")
print(f"Área Quadrado = {area_Quadrado}")
print(f"Área Retângulo = {area_Retangulo}")

