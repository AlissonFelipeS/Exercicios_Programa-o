#Peça vários números ao usuário (encerra com 0) e informe qual foi o maior número digitado.

#Peça o nome do usuario
nome = input("Digite seu nome: ")
maior_numero = 0 #Variável usada como memoria

#Loop para saber maior numero
while True:
    A = int(input(f" {nome} digite um numero,se encontrarmos um maior iremos memorizar, para encerrar digite '0' : "))
    
    if A==0:
        print("Numero 0 digitado, encerrando programa")
        break
    
    if A > maior_numero:
        print (f" {nome} encontramos um maior numero")
        maior_numero= A
        
print ("Maior numero é igual a ",  maior_numero)        