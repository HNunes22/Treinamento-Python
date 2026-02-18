import pandas as pd
import re

df = pd.read_csv("../DataSets/house.csv/house.csv")

# Alterar valor

# O que acontece: Localizo na coluna "SellerG" o vendedor Nelson, e altero para Ronalds

df.loc[df["SellerG"] == "Nelson", "SellerG"] = "Ronalds"


#O que acontece: Estou localizando vendedor "Ronalds" e estou alterando
# todos os Methodos de pagamento dele para "Pending"
df.loc[df["SellerG"] == "Ronalds", ["Method"]] = "Pending"

print(df[["SellerG", "Method"]])