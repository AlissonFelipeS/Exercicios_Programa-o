#Peça várias notas ao usuário (encerra quando digitar -1) e calcule a média das notas válidas.

nome = input("Digite seu nome: ")
numero_de_notas = 0
soma= 0

while True:
    A = float(input(f"{nome}, digite a nota do aluno, para sair digite -1: "))
    if A == -1:
        print (f"{nome} saindo do programa")
        break
    
    if A>=0:
        print ("Nota válida adicionando a média")
        soma = soma + A
        numero_de_notas +=1
        
print ("Média final: ", soma/numero_de_notas)        
        