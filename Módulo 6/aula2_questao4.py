import random

quantidade_elementos1 = int(input("Digite a quantidade de elementos da lista 1: "))
print(quantidade_elementos1)
lista1 = [int(input(f"Digite o {i+1}º elemento da lista 1: ")) for i in range(quantidade_elementos1)]



quantidade_elementos2 = int(input("Digite a quantidade de elementos da lista 2: "))
print(quantidade_elementos2)
lista2 = [int(input(f"Digite o {i+1}º elemento da lista 2: ")) for i in range(quantidade_elementos2)]

lista_intercalada = []

for i in range(min(quantidade_elementos1, quantidade_elementos2)):
        lista_intercalada.append(lista1[i])
        lista_intercalada.append(lista2[i])

if quantidade_elementos1 > quantidade_elementos2:
        lista_intercalada.extend(lista1[min(quantidade_elementos1, quantidade_elementos2):])
elif quantidade_elementos2 > quantidade_elementos1:
        lista_intercalada.extend(lista2[min(quantidade_elementos1, quantidade_elementos2):])

print("Lista intercalada:", " ".join(map(str, lista_intercalada)))