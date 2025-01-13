# Entrada de dados:
N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))

# Processamento:
diferenca_absoluta = abs(N1 - N2)
diferenca_arredondada = round(diferenca_absoluta, 2)

# Resultado
print(f"A diferença absoluta entre os números é: {diferenca_arredondada}  ")