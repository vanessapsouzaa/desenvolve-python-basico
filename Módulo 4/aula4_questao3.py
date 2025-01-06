# Leitura das notas
n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))

# Cálculo da média
m = (n1 + n2 + n3) / 3

# Verificação da média
if m >= 60:
    print("Aprovado")
else:
    if m >= 40:
        print("Recuperação")
    else:
        print("Reprovado")

# Imprime "Fim" ao final do processo
print("Fim")