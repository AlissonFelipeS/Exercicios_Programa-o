#Crie um programa que: leia 12 números inteiros e armazene-os em uma lista, exiba os números em ordem
#crescente, exiba os números em ordem decrescente, informe quantos números são pares e quantos são
#ímpares

lista = []
c = 12
while True:
    if c == 0 :
        print("A lista chegou ao fim")
        break
    else:
        N = int(input(f"Digite 12 numeros inteiros, faltam {c}: "))
        c -= 1
        lista.append(N)

lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

contador_par = 0
contador_impar = 0

for numero in lista:
    if numero % 2 == 0:
        contador_par += 1
for numero in lista:
    if numero % 2 == 1:
        contador_impar += 1
print("Numeros pares: ", contador_par)
print("Numeros impares: ", contador_impar)

