import pandas as pd

datas = pd.read_csv("../DataSets/fifa.csv/fifa.csv")  # Ler os dados em csv

print(datas.head(3)) # Mostrar os três primeiros / Padrão: 5
print()
print(datas.tail(3)) # Mostrar os três ultimos / Padrão: 5
print()
print(datas.columns) # Mostrar o nome das colunas
print()
print(datas.index) # Mostrar a quantidade de colunas (inicio = 0, fim = 18207 , em quanto em quanto = 1)
print()
print(datas['Name']) # Mostrar apenas a coluna "Names"
print()
print(datas[['Nationality', 'Name']]) # Mostrar duas colunas, a ordem influência
print()
print(datas.iloc[143]) # Puxar jogador pelo index na tabela
print()
print(datas.iloc[0:6])  # Puxar os jogadores de index 0 até 6
print()
print(datas.iloc[2, 2]) # Puxar o dado que está na linha 2 (index) na coluna 2 (index)