#Crie duas listas com 5 números cada. Depois: informe quais valores aparecem nas duas listas, informe
#quais valores são exclusivos de cada lista.

lista1 = []
lista2 = []
lista_1_isolados = []
lista_2_isolados = []
lista_conjunta = []
contador = 5
contador2 = 5

while True:
    N1 = int(input("Digite valores de numeros inteiros: "))
    if contador > 0:
        print("Numero adicionado")
        lista1.append(N1)
        contador -= 1
    else:
        print("Lista 1 chegou ao limite, numero nao adicionado")
        break

while True:
    N2 = int(input("Digite valores de numeros inteiros: "))
    if contador2 >0:
        print("Numero adicionado")
        lista2.append(N2)
        contador2 -= 1
    else:
        print("Lista 2 chegou ao limite, numero nao adicionado")
        break

for numero in lista1:
    if numero in lista1 and numero in lista2:
        lista_conjunta.append(numero)
for numero in lista1:
    if numero not in lista2:
        lista_1_isolados.append(numero)
for numero in lista2:
    if numero not in lista1:
        lista_2_isolados.append(numero)

print("Lista de numeros que aparece nas duas listas: ", lista_conjunta)
print("Lista isolados: ", lista_1_isolados)
print("Lista 2 isolados: ", lista_2_isolados)