numero = (input("Digite seu numero: "))
if len(numero) == 8:
    numero = "9" + numero

elif len(numero) == 9:
    if numero[0] != '9':
        print("O número já tem 9 dígitos, mas o primeiro dígito não é 9!")

numero_formatado = numero[:5] + '-' + numero[5:]
print(f"Número formatado: {numero_formatado}")

