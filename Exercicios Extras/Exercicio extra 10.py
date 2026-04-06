#Converter numero para inteiro, verificar se é par alto ou par baixo, impar ou não é numero
A = input("Digite o valor desejado")

try:
    numero_int = int(A)
    if (numero_int%2==0) and (numero_int>100):
        print("Par alto")
    elif(numero_int%2==0) and (numero_int<100):
        print("Par baixo")
    else:
        print("Numero impar")
except ValueError:
    print ("Valor não é numero inteiro")

input("Aperte ENTER para fechar a janela...")