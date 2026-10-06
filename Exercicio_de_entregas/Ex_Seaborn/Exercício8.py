import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o dataset
df = pd.read_csv('space.csv', sep=';')

#Aplicando o filtro
costMaiorZero = df[df[' Cost'] > 0]

#Gerando o gráfico
sns.boxplot(
    data=costMaiorZero,
    x='Status Rocket',
    y=' Cost'
)
plt.show()