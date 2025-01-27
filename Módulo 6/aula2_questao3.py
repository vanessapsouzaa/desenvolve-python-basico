import random
from collections import Counter

lista1 = [random.randint (0,50) for i in range(20)]
lista2 = [random.randint (0,50) for i in range(20)]
interseccao = list(set(lista1) & set(lista2))

print("Lista 1: ", sorted (lista1))
print("Lista 2: ", sorted (lista2))
print("Intersecção (ordenada):", sorted (interseccao))

contagem_lista1 = Counter(lista1)
contagem_lista2 = Counter(lista2)

for item in interseccao:
    print(f"{item}: (lista1={contagem_lista1[item]}, lista2={contagem_lista2[item]})")