#Faça um programa que leia uma matriz 3x3 de inteiros e multiplique os elementos da diagonal
#principal da matriz por um número k. Imprima a matriz na tela antes e depois da multiplicação

matriz =[]

for j in range (3):
    matriz.append([2,3,4])

print ("Matriz antes da multiplicação")
for c in matriz:
    print (c)

matriz [0][0] *= 3
matriz [1][1] *= 3
matriz [2][2] *= 3

print ("Matriz depois da multiplicação")
for c in matriz:
    print(c)

