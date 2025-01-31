import re

def verificar_palindromo(frase):
    # Remover espaços, pontuação e converter tudo para minúsculas
    frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()
    
    # Verificar se a frase é igual ao seu reverso
    return frase_limpa == frase_limpa[::-1]

def main():
    while True:
        # Solicitar uma frase ao usuário
        frase = input("Digite uma frase (ou 'Fim' para encerrar): ")
        
        # Se o usuário digitar 'Fim', encerra o programa
        if frase.lower() == 'fim':
            print("Programa encerrado.")
            break
        
        # Verificar se a frase é um palíndromo
        if verificar_palindromo(frase):
            print("A frase é um palíndromo!")
        else:
            print("A frase não é um palíndromo.")

# Chama a função principal
main()