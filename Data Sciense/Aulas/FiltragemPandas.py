import pandas as pd

datas = pd.read_csv("../DataSets/fifa.csv/fifa.csv")  # Ler os dados em csv

# Filtrar pela nacionalidade

print(datas.loc[datas['Nationality'] == 'Brazil'])

print()

# Filtrar em ordem alfabética

print(datas.sort_values('Name'))