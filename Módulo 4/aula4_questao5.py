# Leitura do número de respondentes
N = int(input("Digite a quantidade de respondentes: "))

# Inicializa a soma das idades
soma_idades = 0

# Leitura das idades e cálculo da soma
for i in range(N):
    idade = int(input(f"Digite a idade do respondente {i+1}: "))
    soma_idades += idade

# Cálculo da média
media_idades = soma_idades / N

# Impressão da média
print(f"A média das idades é: {media_idades:.2f}")