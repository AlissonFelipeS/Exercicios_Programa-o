#Peça um número e mostre a tabuada dele de 1 a 10.

#Pede nome para o cliente
nome = input("Digite seu nome: ")

#Digite o numero que deseja saber a tabuada
A = int(input(f"{nome} digite o numero que deseja saber a tabuada: "))
C= 0 #Contador para tabuada

#Loop para tabuada
while True:
    if C<11:
        print(f"Tabuada de {A}*{C} é =", A * C)
        C +=1 #Adciona mais 1 ao contador
    else:
        print("Tabuda chegouao fim")
        break

print(f"{nome} obrigado por usar nosso programa")