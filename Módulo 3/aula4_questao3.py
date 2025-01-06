# Entrada de dados:
ano = int(input("Digite um ano: "))

# Processamento:
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print(f"O ano de {ano} é Bissexto.")
else:
     print(f"O ano de {ano} não é Bissexto")

