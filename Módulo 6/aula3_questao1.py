import random

numeros = []
while len(numeros) < 4:
    num = int(input("Digite um número inteiro: "))
    numeros.append(num)

print("Lista original:", numeros)

print("Os 3 primeiros elementos: ", numeros [3:])

print("Os 2 ultimos elementos: ", numeros [-2:])

print("Lista invertida:", numeros[::-1])

print("Elementos de índice par:", numeros[::2])

print("Elementos de índice ímpar:", numeros[1::2])
