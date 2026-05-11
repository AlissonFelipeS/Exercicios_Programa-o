#Peça um número inteiro positivo N e mostre todos os números de 1 até N usando repetição

nome = input("Digite seu nome")
A = 0
N= int(input(f" {nome}, digite um numero que deseje contar até ele: "))

while A <= N:
    print (A)
    A = A + 1