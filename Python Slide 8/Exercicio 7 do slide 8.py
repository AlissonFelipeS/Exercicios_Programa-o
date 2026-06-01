#Cadastre: nome, preço, quantidade em estoque de 5 produtos utilizando listas. Depois: mostre os
#produtos com estoque menor que 10, informe o produto mais caro

Produto1 = []
Produto2 = []
Produto3 = []
Produto4 = []
Produto5 = []


print("Seja bem vindo")
print("Controle seu estoque por aqui")

while True:

    N = int(input("Digite 0 para sair do estoque, ou digite 1 para continuar: "))

    if N ==0:
        print("Você optou por sair do controle de estoque")
        break
    elif N ==1:
        print("Você optou por continuar")
    else:
        print("Digite uma opção válida")

    while True:
        print("Digite 1- Estoque 1, 2- Estoque 2, 3- Estoque 3, 4- Estoque 4, 5- Estoque 5")
        A = int(input("Digite o numero do estoque : "))

        if A == 1:

            print("Controle a lista 1 de produtos")
            nome1 = str(input("Digite o nome do produto: "))
            Produto1.append(nome1)
            preco1 = float(input("Digite o preço do produto: "))
            Produto1.append(preco1)
            quantidade1 = int(input("Digite o quantidade de produtos: "))
            Produto1.append(quantidade1)
            break

        if A == 2:
            print("Controle a lista 2 de produtos")
            nome2 = str(input("Digite o nome do produto: "))
            Produto2.append(nome2)
            preco2 = float(input("Digite o preço do produto: "))
            Produto2.append(preco2)
            quantidade2 = int(input("Digite o quantidade de produtos: "))
            Produto2.append(quantidade2)
            break


        if A == 3:
            print("Controle a lista 3 de produtos")
            nome3 = str(input("Digite o nome do produto: "))
            Produto3.append(nome3)
            preco3 = float(input("Digite o preço do produto: "))
            Produto3.append(preco3)
            quantidade3 = int(input("Digite o quantidade de produtos: "))
            Produto3.append(quantidade3)
            break

        if A == 4:
            print("Controle a lista 4 de produtos")
            nome4 = str(input("Digite o nome do produto: "))
            Produto4.append(nome4)
            preco4= float(input("Digite o preço do produto: "))
            Produto4.append(preco4)
            quantidade4 = int(input("Digite o quantidade de produtos: "))
            Produto4.append(quantidade4)
            break

        if A == 5:
            print("Controle a lista 5 de produtos")
            nome5 = str(input("Digite o nome do produto: "))
            Produto5.append(nome5)
            preco5= float(input("Digite o preço do produto: "))
            Produto5.append(preco5)
            quantidade5 = int(input("Digite o quantidade de produtos: "))
            Produto5.append(quantidade5)
            break

print("---Este é seu estoque---")
print(Produto1)
print(Produto2)
print(Produto3)
print(Produto4)
print(Produto5)

#Iniciaremos a busca de maior preço e quantidade de estoque menor que 10
maior_preco = 0.0
produto_mais_caro= ""

if len(Produto1) > 0:
    if Produto1[2] < 10:
        print(f" {Produto1[0]} precisa de reposição! Apenas {Produto1[2]} unidades.")
    if Produto1[1] > maior_preco:
        maior_preco = Produto1[1]
        produto_mais_caro = Produto1[0]

if len(Produto2) > 0:
    if Produto2[2] < 10:
        print(f" {Produto2[0]} com estoque baixo")
    if Produto2[1] > maior_preco:
        maior_preco = Produto2[1]
        produto_mais_caro = Produto2[0]

if len(Produto3) > 0:
    if Produto3[2] < 10:
        print(f" {Produto3[0]} com estoque baixo.")
    if Produto3[1] > maior_preco:
        maior_preco = Produto3[1]
        produto_mais_caro = Produto3[0]

if len(Produto4) > 0:
    if Produto4[2] < 10:
        print(f" {Produto4[0]} com estoque baixo.")
    if Produto4[1] > maior_preco:
        maior_preco = Produto4[1]
        produto_mais_caro = Produto4[0]

if len(Produto5) > 0:
    if Produto5[2] < 10:
        print(f" {Produto5[0]} com estoque baixo.")
    if Produto5[1] > maior_preco:
        maior_preco = Produto5[1]
        produto_mais_caro = Produto5[0]

print(f"Produto mais caro: {produto_mais_caro} com o valor de {maior_preco}")

