#Desenvolva um programa que solicite ao usuário a digitação de uma nota entre 0 e 10. Caso o valor
#informado esteja fora desse intervalo, o programa deve exibir
#uma mensagem de erro e solicitar novamente a entrada, repetindo o processo até
#que um valor válido seja informado


A = int(input("Digite um valor numerico de 0 a 10"))

while True:
    if 0 <A> 10:
        print("Digite um numero de 0 a 10")
    else:
        print("Valor informado válido")
        break
