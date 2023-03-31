import pandas as pd

df = pd.read_csv('actors.csv')

grouped_data = df.groupby('Actor')['Number of Movies'].mean()

actor_with_highest_average = grouped_data.idxmax()

print(f'O ator/atriz com a maior média por filme é: {actor_with_highest_average}')

# A lógica pra resolver as questões da 12 pra 15 são bem semelhantes então os códigos vão ficar beeem parecidos mesmo