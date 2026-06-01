#Faça um programa que leia duas matrizes A e B 2x2 de inteiros e imprima a matriz C que é a
#soma das matrizes A e B.

matriz_A = []
matriz_B = []
matriz_C = []

for i in range(2):
    matriz_A.append ([2,3])
    matriz_B.append([3,7])
    matriz_C.append([0,0])

print ("Matriz A:")
for c  in matriz_A:
    print(c)

print ("Matriz B:")
for f in matriz_B:
    print(f)


for i in range(2):
    for j in range(2):
        matriz_C[i][j] = matriz_A[i][j] + matriz_B[i][j]

print ("Matriz C:")
for o in matriz_C:
    print(o)

