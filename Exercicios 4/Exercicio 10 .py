#Defina um número fixo no código. Peça ao usuário para adivinhar até acertar.
#Informe se o palpite é maior ou menor que o número correto.

#Boas vindas
print ("---Bem vindo ao jogo de advinhação---")
print ("--- Tente advinhar o numero de 0 a 100---")
nome = input("Digite seu nome: ") #Usuario insere o nome dele
numero_secreto = 47 #Numero a ser advinhado
tentativas = 4 #Numero de tentativas possiveis (5)

#Só aceita numeros inteiros
try:
    
    #Looping para descobrir numero secreto
    while True:
        
        #Usuário digite o  numero que deseja
        A = int(input(f"{nome} tente advinhar o número secreto: "))
        print (f"{nome}, você ainda tem --{tentativas}-- tentativas ")
        
        #Numero secreto é de 0 a 100
        if A <=100 and A > 0:
        
            if tentativas>0: #Looping de tentativas
                if A > numero_secreto:
                    print ("Numero secreto é menor que o digitado")
                    tentativas -=1
                elif A < numero_secreto:
                    print ("Numero secreto é maior que o digitado")
                    tentativas -=1
                else:
                    print(f"--Parabéns {nome} você acertou o numero secreto--")
                    break
            else:
                print (f"Numero de tentativas máxima atingida, {nome} até a próxima tentativa")
                break
        else:
            print (f" {nome} digite numeros de 0 a 100 somente")
except ValueError:
    print (f"Por favor, {nome} digite só numeros inteiros")
    
print (f"{nome} até a próxima vez")