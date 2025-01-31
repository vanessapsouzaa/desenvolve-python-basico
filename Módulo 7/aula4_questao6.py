import pandas as pd

# Carregar o arquivo CSV com o encoding 'latin-1'
file_path = 'spotify-2023.csv'  # Substitua pelo caminho correto do arquivo baixado
df = pd.read_csv(file_path, encoding='latin-1')

# Exibir as 5 primeiras linhas para inspeção
print(df.head())

# Filtrando as colunas necessárias
df_filtered = df[['track_name', 'artist(s)_name', 'artist_count', 'released_year', 'streams']]

# Filtrando para o intervalo de anos de 2012 a 2022
df_filtered = df_filtered[(df_filtered['released_year'] >= 2012) & (df_filtered['released_year'] <= 2022)]

# Ignorar linhas com aspas no nome da música ou nos artistas (não seguirão o formato padrão)
df_filtered = df_filtered[~df_filtered['track_name'].str.contains('"', na=False)]
df_filtered = df_filtered[~df_filtered['artist(s)_name'].str.contains('"', na=False)]

# Para cada ano, pegar a música com o maior número de streams
top_tracks_by_year = []

for year in range(2012, 2023):
    # Filtra as músicas do ano atual
    df_year = df_filtered[df_filtered['released_year'] == year]
    
    # Encontrar a música com o maior número de streams
    top_track = df_year.loc[df_year['streams'].idxmax()]
    
    # Adiciona a música mais tocada ao resultado
    top_tracks_by_year.append([top_track['track_name'], top_track['artist(s)_name'], top_track['released_year'], top_track['streams']])

# Exibir a lista final
print(top_tracks_by_year)
