import random
numero_aleatorio = random.randint(0, 10)

print("Adivinhe o número entre 1 e 10!")

while True:
    try:
        palpite = int(input("Digite seu palpite: "))

        if palpite < numero_aleatorio:
            print("Muito baixo, tente novamente!")

        elif palpite > numero_aleatorio:
            print("Muito alto, tente novamente!")

        else: 
            print(f"Correto! O número é {numero_aleatorio}.")
            break

    except ValueError:
        print("Por favor, insira um número inteiro válido.")


