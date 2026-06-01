#Leia 10 números inteiros e armazene-os em uma lista. Ao final: mostre todos os valores, informe o maior
#valor, informe o menor valor.

print ("--Bem vindo ao nosso programa--")
nome = input("Digite seu nome: ")
lista = list(map(int,input(f"{nome} digite 10 numeros para adicionar a lista: ").split()))

A = len(lista)

if A > 10 and A==0:
    print ("Voce digitou mais de 10 numeros")
    
B= min(lista)
C= max(lista)

print ("O menor numero da lista é: ",  B)
print ("O maior numero da lista é: ",  C)