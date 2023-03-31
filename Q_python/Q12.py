import pandas as pd

df = pd.read_csv('actors.csv')

print(df.head())

grouped_data = df.groupby('Actor').count()['']

ator_com_mais_filmes = grouped_data.idxmax()
mais_filmes = grouped_data.max()

print(f'O ator/atrix com maior numero de filmes é {ator_com_mais_filmes}, com {mais_filmes} filmes.')
