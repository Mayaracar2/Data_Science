import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("paises.csv", sep=";")
print(df.columns)

#Filtrar a América do Norte
america_norte = df[df["Region"].str.strip() == "NORTHERN AMERICA"]

#Gráfico da taxa de mortalidade
plt.plot(
    america_norte["Country"],
    america_norte["Deathrate"],
    marker="o",
    label="Taxa de mortalidade"
)

#Gráfico da taxa de natalidade
plt.plot(
    america_norte["Country"],
    america_norte["Birthrate"],
    marker="o",
    label="Taxa de natalidade"
)

#Título e nome dos eixos
plt.title("Taxa de Natalidade e Mortalidade - América do Norte")
plt.xlabel("Países")
plt.ylabel("Taxa")

#Exibe a legenda
plt.legend()

#Exibe o gráfico
plt.show()