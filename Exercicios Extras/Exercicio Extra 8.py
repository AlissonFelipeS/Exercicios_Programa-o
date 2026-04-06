#Interprete o numero, se for inteiro dobre, se for real divida pela metade, se nao for numeros exiba invalido
A= input("Digite o numero de A")

try:
    Numero_inteiro = int(A)
    print("O numero é inteiro, entao o dobro é:",2*Numero_inteiro)
    
except ValueError:
    try:
        Numero_real= float(A)
        print("O valor é real, entao dividimos por 2:", Numero_real/2)
    except ValueError:
        print("Tipo Inválido")

input("Aperte ENTER para fechar a janela...")