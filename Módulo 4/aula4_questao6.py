# Leitura do número de experimentos
N = int(input("Digite o número de experimentos registrados: "))

# Inicializa as variáveis de contagem
total_cobaias = 0
total_sapos = 0
total_ratos = 0
total_coelhos = 0

# Leitura dos experimentos e contagem das cobaias
for _ in range(N):
    quantidade, tipo = input().split()
    quantidade = int(quantidade)
    
    # Acumula a quantidade de cobaias para cada tipo
    total_cobaias += quantidade
    if tipo == 'S':
        total_sapos += quantidade
    elif tipo == 'R':
        total_ratos += quantidade
    elif tipo == 'C':
        total_coelhos += quantidade

# Cálculo dos percentuais
percentual_sapos = (total_sapos / total_cobaias) * 100
percentual_ratos = (total_ratos / total_cobaias) * 100
percentual_coelhos = (total_coelhos / total_cobaias) * 100

# Saída dos resultados
print(f"Total de cobaias: {total_cobaias}")
print(f"Total de sapos: {total_sapos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de coelhos: {total_coelhos}")
print(f"Percentual de sapos: {percentual_sapos:.2f} %")
print(f"Percentual de ratos: {percentual_ratos:.2f} %")
print(f"Percentual de coelhos: {percentual_coelhos:.2f} %")