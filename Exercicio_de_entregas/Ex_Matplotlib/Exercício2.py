import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", sep=";")
print(df.columns)

#Utilizamos o contains, porque o tem outras informações junto com o país
empresas_EUA = df[df["Location"].str.contains("USA")]
empresas_China = df[df["Location"].str.contains("China")]

#Contabilizando as empresas únicas
Unicas_EUA = empresas_EUA["Company Name"].unique()
Unicas_China = empresas_China["Company Name"].unique()

#Contabilizando quantos existem
quant_EUA = len(Unicas_EUA)
quant_China = len(Unicas_China)

paises = ["EUA", "China"]
quantidades = [quant_EUA, quant_China]

#Plotando o gráfico
plt.bar(paises, quantidades, color="pink")

plt.xlabel("Países")
plt.ylabel("Quantidade de empresas")
plt.title("Quantidade de empresas espaciais dos EUA e CHINA")

plt.show()
