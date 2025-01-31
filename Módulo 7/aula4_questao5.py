import csv

# Dados sobre os livros
livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 512],
    ["A Menina que Roubava Livros", "Markus Zusak", 2005, 552],
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423],
    ["Harry Potter e a Pedra Filosofal", "J.K. Rowling", 1997, 223],
    ["O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 96],
    ["O Código Da Vinci", "Dan Brown", 2003, 454],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 448]
]

# Abrindo o arquivo CSV para escrita
with open('meus_livros.csv', mode='w', newline='', encoding='utf-8') as file:
    escritor_csv = csv.writer(file)
    
    # Escreve os títulos das colunas
    escritor_csv.writerow(["Título", "Autor", "Ano de publicação", "Número de páginas"])
    
    # Escreve os dados de cada livro
    for livro in livros:
        escritor_csv.writerow(livro)

print("Arquivo 'meus_livros.csv' criado com sucesso!")