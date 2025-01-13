import emoji

# Lista de emojis disponíveis com seus respectivos códigos
emojis_disponiveis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:",
    "😃": ":smiley:",
    "😎": ":sunglasses:",
    "😢": ":cry:",
    "🌟": ":star:",
    "🔥": ":fire:",
    "💡": ":bulb:"
    ""
}

# Apresenta os emojis disponíveis e seus códigos
print("Emojis disponíveis:")
for emoji_visual, emoji_codigo in emojis_disponiveis.items():
    print(f"{emoji_visual} - {emoji_codigo}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e insira um emoji:\n")

# Emojiza a frase usando emoji.emojize() 
frase_emojizada = emoji.emojize(frase_codificada)

# Exibe a frase emojizada
print("\nFrase emojizada:")
print(frase_emojizada)









