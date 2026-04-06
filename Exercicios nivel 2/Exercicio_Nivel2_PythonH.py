#Descubra as especificações do numero
A= int(input("Digite o valor do numero"))
if (A>0) and ((A%2)==0):
	print ("Par positivo")
elif(A>0) and ((A%2)==1):
	print("Impar positivo")
 elif(A<0) and ((A%2)==-2):
	print ("Par negativo")
elif(A<0) and ((A%2)==-1):
	print("Impar negativo")
else:
	print("Numero neutro")
input("Aperte ENTER para fechar a janela...")
