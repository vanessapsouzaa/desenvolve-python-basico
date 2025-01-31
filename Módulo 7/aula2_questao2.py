frase = (input("Digite uma frase: "))

frase_modificada = frase

for vogal in "AEIOUaeiou":
    frase_modificada = frase_modificada.replace(vogal, "*")

print(frase_modificada)