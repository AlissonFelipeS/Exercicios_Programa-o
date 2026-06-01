#Faça um programa que verifique se uma palavra é um palíndromo (ex.: “arara”).

palavra = str(input("Digite uma palavra: "))
palavra_invertida = palavra[::-1]

if palavra_invertida == palavra:
    print("A palavra é um palindromo")
else:
    print("A palavra não é um palindromo")