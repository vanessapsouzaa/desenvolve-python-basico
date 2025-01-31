import re

def validador_senha(senha):
    # Verifica o comprimento da senha
    if len(senha) < 8:
        return False
    
    # Verifica se contém pelo menos uma letra maiúscula e uma letra minúscula
    if not any(c.islower() for c in senha) or not any(c.isupper() for c in senha):
        return False
    
    # Verifica se contém pelo menos um número
    if not any(c.isdigit() for c in senha):
        return False
    
    # Verifica se contém pelo menos um caractere especial
    if not any(c in '@#$%&*!' for c in senha):
        return False
    
    return True

# Exemplo de uso:

senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False