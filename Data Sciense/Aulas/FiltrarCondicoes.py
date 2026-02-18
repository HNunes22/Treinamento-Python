import pandas as pd

df = pd.read_csv("../DataSets/house.csv/house.csv")

# Irá Filtrar uma casa pela quantidade, tipo e preço
filterQuantityRooms = df.loc[(df["Rooms"] == 3) & (df["Type"] == 'h') & (df["Price"] < 1000000)]
print(filterQuantityRooms)
