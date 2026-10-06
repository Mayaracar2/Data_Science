import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Puxando o dataset
titanic = sns.load_dataset('titanic')

#Gerando uma curva de densidade (KDE)
sns.histplot(
    data=titanic,
    x='age',
    hue='sex',
    kde=True
)
plt.show()