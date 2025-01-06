# Entrada de dados:
idade               = int(input("Digite sua idade: "))
jogos_tres_ou_mais  = (input("Já jogou pelo menos 3 jogos de tabuleiro? "))
vitorias            = int(input("Quantos jogos já venceu? "))

# Processamento:
apto_para_ingressar = 16 <= idade <= 18 and jogos_tres_ou_mais and vitorias >= 1

# Resultado:
print(f"Apto para ingressar no clube de jogos de tabuleiro: {apto_para_ingressar}")