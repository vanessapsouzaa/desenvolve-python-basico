# Função para encontrar os anagramas da palavra objetivo
def encontrar_anagramas(frase, palavra_objetivo):
    # Cria um dicionário onde a chave é a palavra ordenada
    # e o valor é uma lista de palavras que são anagramas
    anagramas = []

    # Dividir a frase em palavras
    palavras = frase.split()

    # Ordenar a palavra objetivo
    chave_objetivo = ''.join(sorted(palavra_objetivo))

    # Iterar sobre as palavras na frase
    for palavra in palavras:
        # Ordenar a palavra atual e comparar com a chave da palavra objetivo
        if ''.join(sorted(palavra)) == chave_objetivo:
            anagramas.append(palavra)

    # Exibe os anagramas encontrados
    print(f"Anagramas de '{palavra_objetivo}': {anagramas}")

# Solicita a frase do usuário
frase = input("Digite uma frase: ")

# Solicita a palavra objetivo
palavra_objetivo = input("Digite a palavra objetivo: ")

# Chama a função para encontrar os anagramas
encontrar_anagramas(frase, palavra_objetivo)