# Aplicativo Analista de Imovéis Australianos 16/02

import pandas as pd
import dotenv
import os
import  matplotlib.pyplot as plt
from sqlalchemy import create_engine
from urllib.parse import quote

# Carregar as variáveis para o ambiente
dotenv.load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = quote(os.getenv("DB_PASSWORD"))
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Faz toda a conexão com o banco de dados
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Criar motor da DataBase
engine = create_engine(DATABASE_URL)

# Query

query_all = """
    SELECT * FROM house_prices;
"""

average_price_per_regions = """
    SELECT regioName, AVG(price) AS average_per_region
    FROM house_prices
    GROUP BY regioName;
"""

houses_upTo_500t = """
    SELECT * FROM house_prices
    WHERE price <= 500000;
"""

five_most_expansive_regions = """
    SELECT regioName, AVG(price) AS five_most_expansive_region
    FROM house_prices
    GROUP BY regioName
    ORDER BY five_most_expansive_region DESC
    LIMIT 5;
"""

quantity_houses_in_regions = """
    SELECT regioName, COUNT(*) FROM house_prices
    GROUP BY regioName
    ORDER BY COUNT(*) DESC;
"""

# DataFrames
df_average_price_per_regions = pd.read_sql(average_price_per_regions, engine)
df_houses_up_to_500t = pd.read_sql(houses_upTo_500t, engine)
df_five_most_expansive_regions = pd.read_sql(five_most_expansive_regions, engine)
df_quantity_houses_in_regions = pd.read_sql(quantity_houses_in_regions, engine)

# Criação de Gráfico














