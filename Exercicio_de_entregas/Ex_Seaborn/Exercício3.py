import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o dataset
titanic = sns.load_dataset('titanic')

#Gráfico com análise de distribuição
sns.boxplot(
    data=titanic,
    x='class',
    y='age',
    hue='sex'
)
plt.show()