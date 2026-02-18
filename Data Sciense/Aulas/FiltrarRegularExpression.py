import pandas as pd
import re # Ele ajuda a evitar erros ortográficos

df = pd.read_csv("../DataSets/house.csv/house.csv")

# Aqui irá filtrar as casas que CONTEM os endereços Turner St OU Turner rD
filterForAddress = df.loc[df["Address"].str.contains("turner sT|Turner rD", flags=re.I)]

# Aqui irá filtrar do mesmo jeito só que adicionando uma nova condição

filterForAddressWithPrice = df.loc[df["Address"].str.contains('^59',  flags=re.I) & (df["Price"] < 500000)]

print(filterForAddressWithPrice)