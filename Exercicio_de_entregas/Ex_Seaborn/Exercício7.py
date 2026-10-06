import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o gráfico
df = pd.read_csv("paises.csv", sep=";")
print(df.columns)

#Gerando o gráfico
sns.regplot(
    data=df,
    x='Literacy (%)',
    y='Infant mortality (per 1000 births)',
    line_kws={'color':'purple'}
)
plt.show()