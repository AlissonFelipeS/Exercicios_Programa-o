#Converter para numero inteiro, verificar se é baixo ou alto.
A=input("Digite o valor de A")
try:
    Teste = int(A)
    
    if Teste>10:
        print("Alto")
    else:
        print("Baixo")
        
except ValueError:
    print("Entrada inválida")

input("Aperte ENTER para fechar a janela...")