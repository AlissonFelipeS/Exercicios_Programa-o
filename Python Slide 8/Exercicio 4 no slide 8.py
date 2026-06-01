#Desenvolva um programa que: leia 10 números inteiros e os armazene em uma lista, solicite ao usuário um
#número para remoção, remova todas as ocorrências desse número da lista, exiba a lista atualizada. Caso o
#número não exista na lista, informe ao usuário

contador = 0
lista = []

try:

    while True:
        
        N = int(input("Digite um numero para adicionar a lista: "))
        
        if contador <= 10:
            lista.append (N)
            contador +=1
        else:
            print ("Limite de numeros alcançados")
            break
            
    print ("Segue a lista de numeros:", lista)        
    print ("-" *10)

    
    A = int(input("Digite o valor que deseja retirar da lista: "))
    
    while True:
        if A in lista:
            lista.remove(A)
        else: 
            break
    
    print ("-" *10)
    print("Esta é a lista atualizada" , lista)

            
except ValueError:
    print ("Digite um valor valido")
        