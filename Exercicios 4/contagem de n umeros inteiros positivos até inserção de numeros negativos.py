#Determine a quantidade de números inteiros positivos fornecidos para um
#programa (até a leitura de um inteiro não positivo)

numeros_inteiros = 0
 
while True:
    
    A = int(input("Digite um numero inteiro: "))
    
    if A>0:
        print (A)
        numeros_inteiros +=1
    else:
        print("Digitado um numero negativo")
        break
print (f"Quantidade de numeros inteiros positivos digitados {numeros_inteiros} ")    
         
     