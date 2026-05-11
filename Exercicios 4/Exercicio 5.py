#Peça números ao usuário continuamente e informe se cada número é par ou ímpar. O programa só
#deve parar quando o usuário digitar 0

nome = input("Digite seu nome: ")#Digita nome do cliente


#Loop para verificar par ou impar
while True:
    A = int(input(f" {nome}, digite o valor do numero: "))#Entrada do usuario
    
    #Se a entrada for 0 para o programa
    if A==0:
        print(f"--{A}-- é é 0, fim do programa")
        break
    
    #Se for par ou impar temos saidas
    if A%2 ==0:
        print(f"--{A}-- é numero par")
    elif A%2 == 1:
        print (f"--{A}-- é um numero impar")
  
        
print (f"{nome} digitou para finalizar o programa")