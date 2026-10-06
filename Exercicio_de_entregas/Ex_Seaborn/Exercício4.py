import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o dataset
mpg = sns.load_dataset('mpg')

#Gráfico da análise
sns.regplot(
    data=mpg,
    x='horsepower',
    y='mpg',
    line_kws={'color':'red'}
)

plt.show()