#Verifica valor informado pelo usuário
A= input("Digite o valor de A")
print (type(A))

try:
    Numero= float(A)
    print(Numero/2)
    
except ValueError:
    print("Entrada invalida")

input("Aperte ENTER para fechar a janela...")

