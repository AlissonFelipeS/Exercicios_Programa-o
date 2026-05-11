#Peça números ao usuário até que ele digite 0. Ao final
#informe quantos números positivos e quantos negativos foram digitados

nome = input("Digite seu nome: ")

negativos = 0
positivos = 0

while True:
    A=int(input(f"{nome} digite um numero para contar positivo ou negativo: "))
    if A == 0 :
        print("Obrigado por contar conosco, o programa chegou ao fim")
        break
    elif A>0:
        print ("Adicionou mais um numero positivo")
        positivos +=1
    elif A<0:
        print("Adicionou mais um numero negativo")
        negativos +=1
        
print (f"{nome}, a quantidade de numeros positivos que você digitou foi: {positivos}")
print (f"{nome}, a quantidade de numeros negativos que você digitou foi: {negativos}")