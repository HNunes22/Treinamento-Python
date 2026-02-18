import pandas as pd
import re

df = pd.read_csv("../DataSets/house.csv/house.csv")

# Aqui ele vai tirar uma média de quartos, price, postcode, propertyCount e Distance da tabela por vendedor
df_mean = df.groupby(['SellerG']).mean(numeric_only=True)

# Aqui ele vai somar os 10  vendedores qaue mais venderm
# obs. sem o Head, ele mostra do maior pro menor
df_sum = df.groupby(["SellerG"]).sum().sort_values("Price", ascending=False).head(10)

# Faz a contagem, tipo, Suburb, tal Vendedor tem X casas em N suburbs
df_count = df.groupby(["SellerG"]).count()

print(df_count)