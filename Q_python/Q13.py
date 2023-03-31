import pandas as pd

df = pd.read_csv('actors.csv')

average = df['Number of movies'].mean()

print(f'A média da coluna "Number of movies" é: {average}')