#Receba 15 números inteiros e armazene-os em uma lista. Depois: crie uma lista apenas com números
#pares, crie outra lista apenas com números ímpares, exiba as duas listas.


print ("Bem vindo ao nosso programa")
print ("Coloque 15 numeros para descobrir quais são pares e  quais são impares")


c_n = 0
lista = []
lista_pares = []
lista_impares = []

while c_n <=15:
    N = int(input("Digite aqui o valor dos numeros que voce deseja adicionar a lista: "))
    lista.append(N)
    c_n +=1
    
    if N%2 == 0:
        lista_pares.append(N)
    else:
        lista_impares.append(N)
        
print ("A lista completa é: ", lista)
print ("Os numeros pares são: ", lista_pares)
print ("Os numeros impares são:", lista_impares)