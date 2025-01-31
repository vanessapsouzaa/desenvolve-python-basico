def exibir_data_de_nascimento():
    meses = [
        "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", 
        "setembro", "outubro", "novembro", "dezembro"
    ]

    data_nascimento = (input("Digite uma data de nascimento (dd/mm/aaaa): "))
    dia, mes, ano = data_nascimento.split ('/')

    print(f"Você nasceu em {dia} de {meses[int(mes) - 1]} de {ano}")

exibir_data_de_nascimento()

