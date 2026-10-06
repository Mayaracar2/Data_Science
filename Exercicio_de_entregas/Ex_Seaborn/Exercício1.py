import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o dataset
iris = sns.load_dataset('iris')

#Filtra a espécie
setosa = iris[iris['species'] == 'setosa']
corr = setosa[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']].corr()

#Apresenta a correlação
sns.heatmap(
    corr,
    annot = True,
    fmt='.2f'
)
plt.show()