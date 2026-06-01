#Leia 8 números inteiros e armazene-os em uma lista. Em seguida: solicite um número ao usuário,
#informe se o número está ou não presente na lista

print ("Seja bem vindo")

c_n =0
lista = []

try:
    
    while True:
        N = int (input("Digite um valor para adicionar a lista dos inteiros: "))
        c_n +=1
        
        if c_n <=8:
            lista.append (N)
        else: 
            print("Limite de numeros alcançados")
            break

    print ("-" * 10)
            
    A = int(input("Digite o valor que deseja saber se está ou nao na lista, digite '0' para sair: "))
    
    while True:
        if A in lista:
            print ("O numero está na lista")
            print ("OBRIGADO POR USAR O NOSSO PROGRAMA, VOLTE SEMPRE")
            break
        elif A == 0:
            print ("Voce optou por sair, estaremos no aguardo do seu retorno..")
            break
        else:
            print ("O numero não está na lista")
            
        
except ValueError:
    print ("Digite um numero válido")