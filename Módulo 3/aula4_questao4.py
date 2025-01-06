# Entrada de dados:
distancia_km = int(input("Digite a distância da entrega em quilômetros: "))
peso_kg = float(input("Digite o peso do pacote em quilogramas: "))

# Processamento:
if distancia_km <= 100:
    custo_por_kg = 1.00
elif 101 <= distancia_km <= 300:
    custo_por_kg = 1.50
else:
    custo_por_kg = 2.00


# Resultado:
valor_frete = peso_kg * custo_por_kg

if peso_kg > 10:
    valor_frete += 10.00

print(f"O valor do frete é: R${valor_frete:.2f}")