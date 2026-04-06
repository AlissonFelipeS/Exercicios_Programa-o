#Verificação de multiplos de 5, se for maior que 50 o multiplo é alto, caso contrario baixo
A= int(input("Verifique se é multiplo de 5:"))

if (A%5==0):
    if A>50:
        print("Multiplo alto")
    else:
        print("Multiplo baixo")
else:
    print("Numero não é multiplo")

input("Aperte ENTER para fechar a janela...")