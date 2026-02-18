import pandas as pd

datas = pd.read_csv("../DataSets/fifa.csv/fifa.csv")  # Ler os dados em csv

datas['Total'] = datas['Acceleration'] + datas['Agility'] + datas['Reactions']
# Cria uma nova coluna, a partir do resultado de três dados ao final da tabela

datas = datas[['Name', 'Total']] # Recria a tabela com apenas as colunas name e total

print(datas.sort_values('Total', ascending=False))  # Exibe a tabela para qual jogador co maior total para o menor

# Transformar o arquivo atual em um novo arquivo

datas.to_csv('../AppAnalistaDeImoveis/DataSetsTestes/fifaPlayers.csv', index=False)
