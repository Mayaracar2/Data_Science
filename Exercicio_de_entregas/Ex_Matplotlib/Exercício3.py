import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", sep=";")
print(df.columns)

Roscosmos = df[df["Company Name"] == "Roscosmos"]

sucesso = Roscosmos[Roscosmos["Status Mission"] == "Success"]
falha = Roscosmos[Roscosmos["Status Mission"] == "Failure"]

quant_sucesso = len(sucesso)
quant_falha = len(falha)

quantidades = [quant_sucesso, quant_falha]
status = ["Sucesso", "Falha"]

plt.pie(quantidades, labels=status, autopct='%1.1f%%', colors=["lightpink", "palevioletred"])

plt.title("Missões da Roscosmos")

plt.show()