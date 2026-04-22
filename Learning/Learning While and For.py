#Lista de nota para professora de Analise e Desenvolvimento de Sistemas para saber quantidade de notas
#e quantidade de alunos que tiraram nota maior que 7, nota menor que 7 e zeros

#Inserção do nome da professora
while True:
    nome = input("Digite o seu primeiro nome com apenas letras: ")
    if nome.isalpha():
        print("Bem vinda professora", nome)
        break
print("Prosseguindo com a lista ...")
    
print("-" * 30)

while True:
    #Evitando inserção letras pra inserçao de notas dos alunos e limitando inserção de no maximo 40 notas
    try:
        lista = list(map(float,input("Digite os valores das notas dos alunos,com o limite de 20 notas").split()))
        quantidade= len(lista)
        
        
        if 0<quantidade<=20:
            print("Continue com o processo, quantidade de notas dentro do aceito")
            
            #Adicionando contadores para saber a quantidade de alunos na média e fora dela.
            notas_acimade_7 = 0
            notas_abaixode_7= 0
            notas_0 = 0
            
            #Verificação das notas dos alunos
            for c in lista:
                if c > 7:
                    print("Os numeros maiores que 7 são:", c)
                    notas_acimade_7 += 1 #Notas acima de 7
                        
                elif c < 7 and c>0:
                    print("Os numeros menores que 7 são", c)
                    notas_abaixode_7 +=1 #Notas abaixo de 7
                    
                elif c == 0:
                    print("As notas de 0 são:", c)
                    notas_0 +=1 #Notas 0
                    print("-" * 30)
                    
            print("-" * 30)
            
            #Verificação de média de notas dos alunos
            if notas_abaixode_7 > 15:
                print("Turma com media baixa")
            elif notas_acimade_7 > 15:
                print ("Turma com media alta")
            else:
                print("Turma com média baixissima")
                    
            print("-" * 30)
            print ("As notas acima de 7 são: ", notas_acimade_7 ,"notas")
            print ("As notas abaixo de 7 são: ", notas_abaixode_7 , "notas")
            print ("As notas 0 são: ", notas_0 , "notas")
            
            print("-" * 30)
            
            #Verificação da pontuação máxima
            pontuação_máxima = max (lista)
            print("Pontuação máxima atingida foi: ", pontuação_máxima)
            break
        
        else:
            print("Fora do limite de quantidade")
    
    #Se nao tiver somente numeros entra no except
    except ValueError:
        print("Digite um numero válido, leitura somente de numeros inteiros e reais")
        

