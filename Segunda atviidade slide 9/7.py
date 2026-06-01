# Leia uma matriz 4x4 e informe qual é o maior número armazenado nela

matriz = []
contador = 9

for l in range(3):
    linha = []
    for c in range(3):
        linha.append(int(input(f"Digite um valor, faltam {contador}: ")))

    matriz.append(linha)


maior_absoluto = 0

for linha in matriz:
    maior = max(linha)

    if maior > maior_absoluto:
        maior_absoluto = maior

print(f"O maior valor digitado foi {maior_absoluto}")