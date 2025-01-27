import random
from collections import Counter

lista = [random.randint (-10,10) for i in range(20)]
print("Original:", lista)

max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

for i in range(len(lista)):
    if lista[i] < 0:
        
        j = i
        while j < len(lista) and lista[j] < 0:
            j += 1
        
        negativos_count = j - i
        if negativos_count > max_negativos:
            max_negativos = negativos_count
            inicio_intervalo = i
            fim_intervalo = j
        i = j  
    
# Remover o intervalo com a maior quantidade de negativos
del lista[inicio_intervalo:fim_intervalo]


print("Editada:", lista)
