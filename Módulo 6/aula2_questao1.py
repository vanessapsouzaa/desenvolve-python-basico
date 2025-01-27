import random

numeros = [random.randint(-100, 100) for i in range(20)]

print("Lista ordenada (sem modificar a original):", sorted(numeros))

print("Lista original:", numeros)

print("O maior valor da lista é:", max(numeros))

print("O menor valor da lista é:", min(numeros))


