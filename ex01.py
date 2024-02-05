#Calcular a média de uma lista de números: Crie um programa que receba uma lista de números e retorne a média dos valores presentes na lista.

lista = [1, 2, 3, 4 ,5 ,6]
i = len(lista)
total=0
for n in range(i):
    total += lista[n]
    n+=1
media = total / i
print(f"A média é de {media}")
