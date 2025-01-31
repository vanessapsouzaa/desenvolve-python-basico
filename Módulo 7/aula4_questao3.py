import re

def processar_roteiro():
    # Abre o arquivo 'estomago.txt' para leitura
    with open('estomago.txt', 'r', encoding='latin1') as arquivo:
        # Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

    # 1. Imprimir o texto das primeiras 25 linhas
    print("Primeiras 25 linhas do roteiro:\n")
    for i in range(min(25, len(linhas))):
        print(linhas[i], end='')

    print("\n" + "="*40)

    # 2. Contar o número de linhas no arquivo
    num_linhas = len(linhas)
    print(f"Número de linhas no arquivo: {num_linhas}\n")
    
    print("="*40)

    # 3. Encontrar a linha com maior número de caracteres
    maior_linha = max(linhas, key=len)
    print(f"A linha com maior número de caracteres tem {len(maior_linha)} caracteres.")
    print(f"Conteúdo da linha: {maior_linha}\n")
    
    print("="*40)

    # 4. Contar o número de menções aos personagens "Nonato" e "Íria"
    texto = ''.join(linhas).lower()  # Juntar todas as linhas e converter para minúsculas

    # Usando expressões regulares para contar as menções de "Nonato" e "Íria" (evitar substrings como "iria")
    mencao_nonato = len(re.findall(r'\bnonato\b', texto))
    mencao_iria = len(re.findall(r'\bíria\b', texto))

    print(f"Número de menções a 'Nonato': {mencao_nonato}")
    print(f"Número de menções a 'Íria': {mencao_iria}")

# Chama a função para processar o roteiro
processar_roteiro()