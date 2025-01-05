saldo = 500.0
juros = 1.01

# Atualizando o saldo mês a mês com os juros
saldo = saldo * juros  # Após o primeiro mês
saldo = saldo * juros  # Após o segundo mês
saldo = saldo * juros  # Após o terceiro mês

# Resultado final
print("Após 3 meses meu novo saldo é")
print(saldo)