import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", sep=";")
print(df.columns)

#Como é referente a todas as empresas, eu preciso só verificar os status
ativos = df[df["Status Rocket"] == "StatusActive"]
aposentados = df[df["Status Rocket"] == "StatusRetired"]

quant_ativos = len(ativos)
quant_aposentados = len(aposentados)

#Passando os parâmetros
quantidades = [quant_ativos, quant_aposentados]
status = ["Ativos", "Aposentados"]

plt.pie(quantidades, labels=status, autopct='%1.1f%%',  colors=["lightpink", "palevioletred"])

plt.title("Status dos Foguetes")
plt.show()

