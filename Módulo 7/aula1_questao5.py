frase = (input("Digite uma frase: "))
print(frase)
vogais = ['A', 'E', 'I', 'O', 'U', 'a' , 'e', 'i', 'o', 'u']

contagem_vogais = 0
indices_vogais = []

for i, char in enumerate(frase):
    if char in vogais:
        contagem_vogais += 1
        indices_vogais.append(i)


print(f"{contagem_vogais} vogais")
print(f"Índices {indices_vogais}")