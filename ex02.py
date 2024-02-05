#Verificar se um número é par ou ímpar: Neste exercício, você deve desenvolver um programa que recebe um número como entrada e determina se ele é par ou ímpar

valor = int(input("Digite o valor para saber se ele é par ou impar: "))
if valor % 2 == 0:
    print(f"O valor {valor} é par")
else:
    print(f"O valor {valor} é impar")