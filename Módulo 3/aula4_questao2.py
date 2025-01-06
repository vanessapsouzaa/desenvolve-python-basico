# Entrada de dados:
avaliacao_filme = int(input("Insira a avaliação do filme (1 a 5) 'Duna: Parte Dois': "))

#Processamento e Saída:
if avaliacao_filme == 5:
    print("Excelente!") 
elif avaliacao_filme == 4:
    print("Muito Bom!") 
elif avaliacao_filme == 3:
    print("Bom!") 
elif avaliacao_filme == 2:
    print("Regular.") 
elif avaliacao_filme == 1:
    print("Ruim") 
else:
    print("Avaliação inválida. Por favor, insira um valor entre 1 e 5.")