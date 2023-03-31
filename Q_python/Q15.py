import pandas as pd

df = pd.read_csv('Actors.csv')

frequency = df['#1 Movie'].value_counts()

max_frequency = frequency.max()

most_frequent_movies = frequency.loc[frequency == max_frequency]

print(f'O(s) filme(s) mais frequente(s) é(são): \n{most_frequent_movies}')