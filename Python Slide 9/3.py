#Receba uma frase e substitua todas as ocorrências de uma palavra específica por outra.

frase= str(input("Digite uma frase: "))
print(frase)

palavra = str(input("Digite a palavra que deseja substituir: "))
palavra_nova = str(input("Digite a nova palavra: "))
substituicao = frase.replace (palavra, palavra_nova)


print("A nova frase é:" , substituicao)