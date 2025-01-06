# Dados de entrada
classe = input("Digite a classe do personagem (guerreiro, mago ou arqueiro): ").strip().lower()
forca = int(input("Digite os pontos de força: "))
magia = int(input("Digite os pontos de magia: "))

# Processamento
if classe == "guerreiro":
    valido = forca >= 15 and magia <= 10
elif classe == "mago":
    valido = forca <= 10 and magia >= 15
elif classe == "arqueiro":
    valido = 5 < forca <= 15 and 5 < magia <= 15
else:
    valido = False  # Classe inválida

# Imprime o resultado
print(valido)