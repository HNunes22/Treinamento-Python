import matplotlib.pyplot as plt
import pandas as pd

# Pegar a tabela de Gas
gas = pd.read_csv('../DataSets/gas_price/gas_prices.csv')

# Criação de caracteristicas do gráfico

    # Dar um titulo ao gráfico
plt.title('Value of the Gas in US$')

    # Dar as informações ao gráfico # OBS. 'r.-' R = "Red", . = Delimitador, - = Formato do traço

list_country = ["Japan", "USA", "Germany", "Canada", "Mexico", "Italy"]

for country in gas.columns:
    if country in list_country:
        plt.plot(gas["Year"], gas[country], label=country, marker='.')

'''plt.plot(gas["Year"], gas["Australia"], 'y.-',label="Australia")
plt.plot(gas["Year"], gas["USA"], 'b.-',label="USA")
plt.plot(gas["Year"], gas["Japan"], 'r.-',label="Japan")
plt.plot(gas["Year"], gas["Germany"], 'g.-',label="Germany")'''

    # Formatar o eixo-x, nesse caso como tem bastante anos, foi formatado [::3] pule de três em três anos
plt.xticks(gas["Year"][::3])

    # Dar nome aos eixos: y e x
plt.ylabel("US$")
plt.xlabel("Years")


# Gerar o gráfico

plt.legend()
plt.savefig("countryGasPrices.png")
plt.show()
