#Peça números ao usuário e some-os. O programa deve parar quando o usuário digitar um número
#negativo. Ao final, mostre a soma total.

nome = input("Digite seu nome: ")
print("Você deverá digitar números inteiros para somar,se digitar um negativo ou digite um texto para sair do programa")

soma = 0

try:
    
    while True:
    
        B= int(input(f" {nome}, digite o numero que deseja somar: "))
    
        if B > 0:
            print (f"{nome} numero aceito, adicionando ao calculo")
            soma = soma + B
        elif B<0:
            print("Numero negativo digitado, parando soma")
            break
    
        
except ValueError:
    print("Você digitou um texto")
    
    
    
print ("Valor da soma total é", soma)        