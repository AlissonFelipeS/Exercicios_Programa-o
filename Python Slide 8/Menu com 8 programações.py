#Criando um menu para entrar em 8 codigos de testes

#Loop para escolha de 8 possiveis codig
while True:
    print("=== MENU PRINCIPAL ===")
    print("1 - Lista de inteiros, informar menor e maior valor")
    print("2 - Lista de inteiros, numeros pares e impares")
    print("3 - Lista de inteiros e depois verificação manual")
    print("4 - Faça uma lista e depois remova qualquer numero")
    print("5 - Faça uma lista e verifique os positivos, negativos e zeros")
    print("6 - Faça duas listas e verifique os numeros entre elas")
    print("7 - Faça um controle de estoque")
    print("8 - Fala uma lista para organizar em forma crescente e descrecente")
    print("0 - Sair do Programa")

    opcao = int(input("Escolha uma opção: ")) #Entrada para escolher codigo

    if opcao == 1: #Escolhendo primeiro código
        print("--- Executando Código 1 ---")

        print("--Bem vindo ao nosso programa--")
        nome = input("Digite seu nome: ")


        while True:
            lista = list(map(int, input(
                f"{nome} digite 10 numeros para adicionar a lista: ").split()))  # Adiciona numeros a lista

            A = len(lista) #Verifica tamanho da lista

            if 0<A<10:
                print("Realizando os calculos")
                break

            else:
                print("Digite a quantidade de numeros corretas")

        B = min(lista)
        C = max(lista)

        print("O menor numero da lista é: ", B)
        print("O maior numero da lista é: ", C)



    elif opcao == 2: #Escolhendo segundo código
        print("--- Executando Código 2 ---")

        print("Bem vindo ao nosso programa")
        print("Coloque 15 numeros para descobrir quais são pares e  quais são impares")

        c_n = 15 #contador de 15 numeros
        lista = [] #lista total
        lista_pares = [] #lista pares
        lista_impares = [] #lista impar

        while c_n > 0: #Uso do contador para limitar até quinze numeros
            N = int(input("Digite aqui o valor dos numeros que voce deseja adicionar a lista: "))
            lista.append(N) #Adicionando a lista total
            c_n -= 1

            if N % 2 == 0:
                lista_pares.append(N) #Adicionando a lista de pares
            else:
                lista_impares.append(N) #Adicionando a lista de impares

        print("A lista completa é: ", lista) #imprime lista completa
        print("Os numeros pares são: ", lista_pares) #imprime lista de pares
        print("Os numeros impares são:", lista_impares) #imprime lista de impares

    elif opcao == 3: #Escolhendo codigo 3
        print("--- Executando Código 3 ---")

        print("Seja bem vindo")

        c_n = 8 #Contador de numeros inteiros
        lista = [] #Lista total

        try: #Se inserir textos, protege o codigo

            while True: #Loop de adição de numeros inteiros
                N = int(input(f"Digite um valor para adicionar a lista dos inteiros, faltam {c_n} numeros para adicionar"
                              f" a lista: "))
                c_n -= 1

                if c_n > 0:
                    lista.append(N)
                else:
                    print("Limite de numeros alcançados")
                    break #Se alcançar 8 numeros inteiros quebra loop

            print("-" * 10)

            #=============================================================================================
            #ABAIXO ESTÁ A VERIFICAÇÃO DE NUMEROS QUE PERTENCEM A LISTA
            #=============================================================================================


            A = int(input("Digite o valor que deseja saber se está ou nao na lista, digite '0' para sair: "))

            while True: #Loop para descobrir numero da lista
                if A in lista:
                    print("O numero está na lista")
                    print("OBRIGADO POR USAR O NOSSO PROGRAMA, VOLTE SEMPRE")
                    break
                elif A == 0: #Sair do loop digitando 0
                    print("Voce optou por sair, estaremos no aguardo do seu retorno..")
                    break
                else:
                    print("O numero não está na lista")


        except ValueError:
            print("Digite um numero válido")

    elif opcao == 4: #Escolhendo codigo 4
        print("--- Executando codigo 4 ---")

        contador = 10 #Contador de numeros inteiros, limite de 10
        lista = []

        try:

            while True: #Loop para compor a lista com 10 numeros inteiros

                N = int(input("Digite um numero para adicionar a lista: "))

                if contador > 0:
                    lista.append(N) #Adicionando a lista
                    contador -= 1
                else:
                    print("Limite de numeros alcançados")
                    break #Quantidade alcançada quebra o Loop

            print("Segue a lista de numeros:", lista) #Imprime a lista
            print("-" * 10)

            A = int(input("Digite o valor que deseja retirar da lista: ")) #Escolhendo numero para remover

            while True: #Loop para remover numero da lista
                if A in lista:
                    lista.remove(A)
                else:
                    break

            print("-" * 10)
            print("Esta é a lista atualizada", lista) #Imprime lista atualizada


        except ValueError:
            print("Digite um valor valido")

    elif opcao == 5: #Escolhendo codigo 5
        print("--- Executando codigo 5 ---")

        limite_contagem = 20 #Contador de numeros inteiros
        lista = [] #Lista total
        lista_pares = 0 #Lista pares
        lista_impares = 0 #Lista impares
        lista_0 = 0 #Lista de 0

        while True: #Loop para adicionar numeros a lista
            N = int(input("Digite um numero para adicionar a lista: "))
            if limite_contagem > 0:
                lista.append(N)
                limite_contagem -= 1
            else:
                print("Quantidade de numeros atingida")
                break

            #===========================================================
            #Verificação de tipo de numero
            #===========================================================


            if N == 0: #Numero 0
                lista_0 += 1
            elif N % 2 == 1: #Numero impar
                lista_impares += 1
            elif N % 2 == 0: #Numero par
                lista_pares += 1

        print("-" * 30)
        print("Numeros da lista: ", lista)
        print("Quantidade de numeros pares: ", lista_pares)
        print("Quantidade de numeros impares: ", lista_impares)
        print("Quantidade de numeros 0: ", lista_0)


    elif opcao == 6: #Escolhendo codigo 6
        print("--- Executando codigo 6 ---")

        lista1 = []
        lista2 = []
        lista_1_isolados = [] #Lista que pertecem so a 1
        lista_2_isolados = [] #Lista que pertencem so a 2
        lista_conjunta = [] #Lista de numeros que aparecem nas duas listas
        contador = 5 #Contador lista 1
        contador2 = 5 #Contador lista 2

        while True: #Loop para numeros inteiros da lista 1
            N1 = int(input("Digite valores de numeros inteiros: "))
            if contador > 0:
                print("Numero adicionado")
                lista1.append(N1)
                contador -= 1
            else:
                print("Lista 1 chegou ao limite, numero nao adicionado")
                break

        while True: #Lista para numeros inteiros da lista 2
            N2 = int(input("Digite valores de numeros inteiros: "))
            if contador2 > 0:
                print("Numero adicionado")
                lista2.append(N2)
                contador2 -= 1
            else:
                print("Lista 2 chegou ao limite, numero nao adicionado")
                break

        for numero in lista1: #Loop para verificar se numero está nas duas listas
            if numero in lista1 and numero in lista2:
                lista_conjunta.append(numero)
        for numero in lista1: #Loop para verificar se numero está somente na lista 1
            if numero not in lista2:
                lista_1_isolados.append(numero)
        for numero in lista2: #Loop para verificar se numero está somente na lista 2
            if numero not in lista1:
                lista_2_isolados.append(numero)

        print("Lista de numeros que aparece nas duas listas: ", lista_conjunta)
        print("Lista isolados: ", lista_1_isolados)
        print("Lista 2 isolados: ", lista_2_isolados)

    elif opcao == 7: #Escolhendo codigo 7

        #Controle de estoque de 5 produtos

        print("--- Executando codigo 7 ---")

        Produto1 = []
        Produto2 = []
        Produto3 = []
        Produto4 = []
        Produto5 = []

        print("Seja bem vindo")
        print("Controle seu estoque por aqui")

        while True: #Loop para entrar no controle de estoque

            N = int(input("Digite 0 para sair do estoque, ou digite 1 para continuar: "))

            if N == 0:
                print("Você optou por sair do controle de estoque")
                break
            elif N == 1:
                print("Você optou por continuar")
            else:
                print("Digite uma opção válida")

            while True: #Loop para escolher qual lista quer entrar
                print("Digite 1- Estoque 1, 2- Estoque 2, 3- Estoque 3, 4- Estoque 4, 5- Estoque 5")
                A = int(input("Digite o numero do estoque : "))

                if A == 1: #Escolhendo lista 1
                    print("Controle a lista 1 de produtos")
                    nome1 = str(input("Digite o nome do produto: "))
                    Produto1.append(nome1)
                    preco1 = float(input("Digite o preço do produto: "))
                    Produto1.append(preco1)
                    quantidade1 = int(input("Digite o quantidade de produtos: "))
                    Produto1.append(quantidade1)
                    break

                if A == 2: #Escolhendo lista 2
                    print("Controle a lista 2 de produtos")
                    nome2 = str(input("Digite o nome do produto: "))
                    Produto2.append(nome2)
                    preco2 = float(input("Digite o preço do produto: "))
                    Produto2.append(preco2)
                    quantidade2 = int(input("Digite o quantidade de produtos: "))
                    Produto2.append(quantidade2)
                    break

                if A == 3: #Escolhendo lista 3
                    print("Controle a lista 3 de produtos")
                    nome3 = str(input("Digite o nome do produto: "))
                    Produto3.append(nome3)
                    preco3 = float(input("Digite o preço do produto: "))
                    Produto3.append(preco3)
                    quantidade3 = int(input("Digite o quantidade de produtos: "))
                    Produto3.append(quantidade3)
                    break

                if A == 4: #Escolhendo lista 4
                    print("Controle a lista 4 de produtos")
                    nome4 = str(input("Digite o nome do produto: "))
                    Produto4.append(nome4)
                    preco4 = float(input("Digite o preço do produto: "))
                    Produto4.append(preco4)
                    quantidade4 = int(input("Digite o quantidade de produtos: "))
                    Produto4.append(quantidade4)
                    break

                if A == 5: #Escolhendo lista 5
                    print("Controle a lista 5 de produtos")
                    nome5 = str(input("Digite o nome do produto: "))
                    Produto5.append(nome5)
                    preco5 = float(input("Digite o preço do produto: "))
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

        #=========================================================================
        # Iniciaremos a busca de maior preço e quantidade de estoque menor que 10
        #=========================================================================


        maior_preco = 0.0 #Variavel para salvar maior preço
        produto_mais_caro = "" #Variavel para salvar produto mais caro

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



    elif opcao == 8: #Escolhendo codigo 8
        print("--- Executando codigo 8 ---")

        lista = []
        c = 12 #Contador
        while True: #Loop de 12 numeros
            if c == 0:
                print("A lista chegou ao fim")
                break
            else:
                N = int(input(f"Digite 12 numeros inteiros, faltam {c}: "))
                c -= 1
                lista.append(N)

        lista.sort() #Colocando  a lista de forma crescente
        print("Lista de forma crescente", lista)
        lista.sort(reverse=True) #Colocando a lista de forma decrescente
        print("Lista de forma decrescente", lista)

        contador_par = 0
        contador_impar = 0

        for numero in lista: #loop para encontrar numeros pares
            if numero % 2 == 0:
                contador_par += 1
        for numero in lista: #loop para encontrar numeros impares
            if numero % 2 == 1:
                contador_impar += 1
        print("Numeros pares: ", contador_par)
        print("Numeros impares: ", contador_impar)



    elif opcao == 0: #Usuario escolher sair do programa geral
        print("Saindo do sistema...")
        break  # Desliga o loop do menu

    else: #Necessário uma opção válida
        print("Opção inválida! Tente novamente.")