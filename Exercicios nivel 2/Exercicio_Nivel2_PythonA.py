#Verificação de especificações no número
N = int(input("Digite o valor de N"))
if ((N>0) and (N%2 ==0)):
	print("Par positivo")
elif((N<0) and (N%2 ==0)):
	print("Par negativo")
else:
	print("Numero impar")
input("Aperte ENTER para fechar a janela...")
