import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("paises.csv", sep=";")

#Fazer a média da literacy das regiões
media_alfabetizacao = df.groupby("Region")["Literacy (%)"].mean()

#print(media_alfabetizacao)

#Passando os parametros
regioes = media_alfabetizacao.index
medias = media_alfabetizacao.values

#Plotando o gráfico
plt.bar(regioes, medias, color="pink")

plt.xlabel("Regiões")
plt.ylabel("Média da taxa de alfabetização (%)")
plt.title("Média da taxa de alfabetização por região")

plt.xticks(rotation=90)
plt.tight_layout()

plt.show()