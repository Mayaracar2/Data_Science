import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("paises.csv", sep=";")
print(df.columns)

#Pegar países da europa ocidental
europa_ocidental= df[df["Region"].str.strip() == "WESTERN EUROPE"]

#Plotando os dados
plt.plot(
    europa_ocidental["Country"],
    europa_ocidental["GDP ($ per capita)"],
    marker="*",
    color = "pink",
    linestyle = "-",
    label="GDP per capita"
)

plt.plot(
    europa_ocidental["Country"],
    europa_ocidental["Phones (per 1000)"],
    marker="o",
    color ="purple",
    linestyle="--",
    label="Phones (per 1000)"
)

plt.legend()
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()