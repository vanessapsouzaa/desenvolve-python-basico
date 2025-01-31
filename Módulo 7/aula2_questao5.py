import random

def embaralhar_palavras(frase):
    palavras = frase.split()  # Divide a frase em palavras
    nova_frase = []  # Lista para armazenar as palavras embaralhadas

    for palavra in palavras:
        if len(palavra) > 3:
            # Para palavras com mais de 3 caracteres, embaralhar as letras internas
            primeira_letra = palavra[0]
            ultima_letra = palavra[-1]
            letras_internas = list(palavra[1:-1])
            random.shuffle(letras_internas)  # Embaralha as letras internas
            palavra_embaralhada = primeira_letra + ''.join(letras_internas) + ultima_letra
            nova_frase.append(palavra_embaralhada)
        else:
            # Para palavras pequenas (com 3 ou menos caracteres), não embaralha
            nova_frase.append(palavra)
    
    # Junta as palavras de volta em uma frase
    return ' '.join(nova_frase)

# Exemplo de uso:

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)