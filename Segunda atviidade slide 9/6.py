# Crie uma matriz 3x3 preenchida pelo usuário e exiba todos os valores na tela.

matriz = []
contador = 9
for l in range (3):
    linhas = []
    for i in range (3):
        linhas.append(int(input(f"Digite os numeros da matriz, faltam {contador}: ")))
        contador -= 1
    matriz.append(linhas)

for linha in matriz:
    print(linha)