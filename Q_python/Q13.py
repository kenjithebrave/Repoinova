import pandas as pd

df = pd.read_csv('actors.csv')

average = df['Number of Movies'].mean()

print(f'A média da coluna "Number of Movies" é: {average}')