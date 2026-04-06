#Exibir Resto da divisao por 3 em decrescencia
A= int(input("Digite o valor de A"))
B= int(input("Digite o valor de B"))
C= int(input("Digite o valor de C"))

D= (A%3)
E= (B%3)
F= (C%3)

if (D>E) and (D>F):
    if(E>F):
        print(D,E,F)
    else:
        print (D,F,E)
elif (E>D) and (E>F):
    if(D>F):
        print (E,D,F)
    else:
        print(E,F,D)
elif (F>E) and (F>D):
    if(E>D):
        print(F,E,D)
    else:
        print(F,D,E)
        
        
