import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("space.csv", sep=";")
print(df.columns)

#Filtro o sucesso e a falha
sucesso = df[df["Status Mission"] == "Success"]
falha = df[df["Status Mission"] == "Failure"]

#Agrupar as empresas quje obtiveram sucesso e falha
sucesso_por_empresa = sucesso.groupby("Company Name").count()["Status Mission"]
falha_por_empresa = falha.groupby("Company Name").count()["Status Mission"]

#Ordenar do maior para o menor
sucesso_por_empresa = sucesso_por_empresa.sort_values(ascending=False)
falha_por_empresa = falha_por_empresa.sort_values(ascending=False)

#Pegamos os 5 primeiros
top5_sucesso = sucesso_por_empresa.head(5)
top5_falha = falha_por_empresa.head(5)

#print(top5_sucesso)
#print(top5_falha)

#Função subplot() = quant de linha, quant de colunas e posição deste gráfico
#Gráfico da esquerda (sucesso)
plt.subplot(1,2,1)
#Ajustar os espaços entre os gráficos
plt.subplots_adjust(wspace=0.4)

plt.bar(
    top5_sucesso.index,
    top5_sucesso.values,
    color="pink"
)

plt.title("5 empresas com mais sucessos")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

#Gráfico da direita (Falha)
plt.subplot(1,2,2)
plt.subplots_adjust(wspace=0.4)

plt.bar(
    top5_falha.index,
    top5_falha.values,
    color="purple"
)

plt.title("5 empresas com mais falha")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
