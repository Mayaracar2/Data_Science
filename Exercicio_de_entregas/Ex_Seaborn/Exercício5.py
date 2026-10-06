import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o dataset
df = pd.read_csv("paises.csv", sep=";")
print(df.columns)

#Aplicando o filtro
AL_EO = df[df['Region'].isin(['LATIN AMER. & CARIB    ', 'WESTERN EUROPE                     '])]
#Gerando o gráfico
sns.boxplot(
    data=AL_EO,
    x='Region',
    y='GDP ($ per capita)'
)
plt.show()