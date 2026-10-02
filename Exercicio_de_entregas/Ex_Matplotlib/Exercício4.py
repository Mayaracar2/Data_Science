import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", sep=";")
print(df.columns)

#Todas as missões com falhas
falhas = df[df["Status Mission"] == "Failure"]

#Conta quantas missões existem em cada grupo
falhasPorEmpresa = falhas.groupby("Company Name").count()["Status Mission"]
print(falhasPorEmpresa)

#Ordenar do maior para o menor
falhasPorEmpresa = falhasPorEmpresa.sort_values(ascending=False)

#Mostra os 5 com mais falhas
top5 = falhasPorEmpresa.head(5)

#Passando o padrão
empresas = top5.index
quantidade = top5.values

plt.bar(empresas, quantidade, color="pink")

plt.xlabel("Empresas")
plt.ylabel("Quantidade de falhas")
plt.title("5 empresas com mais missões que falharam")

#Ajuste para o nome não ficar grudado
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
