#Verificar se numero é positivo e multiplo de 3 e 2
A= int(input("Digite o valor de A"))
if (A>0):
    if ((A%2)==0) and ((A%3)==0):
        print ("Multiplo de 2 e 3")
    else:
        print ("Não atende")
else:
    print("Numero inválido")

input("Aperte ENTER para fechar a janela...")
    