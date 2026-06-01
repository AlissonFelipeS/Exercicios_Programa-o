#Leia 20 números inteiros e armazene-os em uma lista. Depois: conte quantos números são positivos
#conte quantos são negativos, conte quantos são iguais a zero

limite_contagem = 20
lista= []
lista_pares = 0 
lista_impares = 0 
lista_0 = 0

while True:
    N= int(input("Digite um numero para adicionar a lista: "))
    if limite_contagem > 0:
        lista.append(N)
        limite_contagem -=1
    else:
        print("Quantidade de numeros atingida")
        break
    if N == 0:
        lista_0 +=1
    elif N%2 == 1:
        lista_impares +=1
    elif N%2 ==0:
        lista_pares +=1
        
print ("-" *30)
print ("Numeros da lista: ", lista)
print ("Quantidade de numeros pares: ", lista_pares)
print ("Quantidade de numeros impares: ", lista_impares)
print ("Quantidade de numeros 0: ", lista_0)
