#Crie um programa que receba uma palavra e mostre quantas vogais existem nela

nome = str(input("Digite um palavra: "))
vogais = ["a", "e", "i", "o", "u"]
contador= 0

for c in nome.lower():
    if c in vogais:
        contador += 1

print(f"Existem {contador} vogais nesta palavra")