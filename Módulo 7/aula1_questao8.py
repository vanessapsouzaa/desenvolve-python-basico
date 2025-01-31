def calcular_digito(cpf_parcial, multiplicadores):
    soma = sum(int(cpf_parcial[i]) * multiplicadores[i] for i in range(len(cpf_parcial)))
    resto = soma % 11
    if resto < 2:
        return 0
    else:
        return 11 - resto

def validar_cpf(cpf):
    # Remover pontos e hífen
    cpf = cpf.replace('.', '').replace('-', '')
    
    # Verifica se o CPF tem 11 caracteres e se todos os caracteres são dígitos
    if len(cpf) != 11 or not cpf.isdigit():
        return "Inválido"
    
    # Primeiro dígito verificador (CPF sem os dois últimos dígitos)
    cpf_parcial = cpf[:9]
    
    # Multiplicadores para o primeiro dígito
    multiplicadores_primeiro = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    primeiro_digito = calcular_digito(cpf_parcial, multiplicadores_primeiro)
    
    # Segundo dígito verificador (CPF sem o último dígito)
    cpf_parcial = cpf[:10]
    
    # Multiplicadores para o segundo dígito
    multiplicadores_segundo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    segundo_digito = calcular_digito(cpf_parcial, multiplicadores_segundo)
    
    # Verificar se os dígitos calculados são iguais aos fornecidos
    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        return "Válido"
    else:
        return "Inválido"

# Solicitar CPF ao usuário
cpf = input("Digite o CPF no formato XXX.XXX.XXX-XX: ")

# Validar CPF
resultado = validar_cpf(cpf)

# Exibir o resultado
print(resultado)