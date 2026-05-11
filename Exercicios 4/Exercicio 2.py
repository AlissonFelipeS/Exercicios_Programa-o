#Peça ao usuário para digitar uma senha. Continue solicitando até que ele acerte a senha correta
#(defina uma senha fixa no código)

senha = "jubileu123"
nome = input("Digite seu nome: ")

while True:
    A = input(f" Seja muito bem vindo, {nome}, por favor, digite sua senha: ")
    
    if A == senha:
        print(f" {nome}, sua senha foi aceita, prossiga com o programa...")
        break
    else:
        print(f" {nome}, infelizmente sua senha está incorreta, tente novamente...")
        
print (f"{nome}, obrigado por escolher a nossa empresa, que você tenha a melhor experiência possível")        