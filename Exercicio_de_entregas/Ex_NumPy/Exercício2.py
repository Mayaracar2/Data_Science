#Exercício 4
import numpy as np

mtz = np.array([[5,3],[7,8],[8,19],[23,65],[1,25]])
print(mtz)
print(mtz.shape) #Mostra o tamanho

tamanho = mtz.shape
multiplicacao = tamanho[0] * tamanho[1] #Coluna por linha

if(multiplicacao % 2 == 0):
    print("Pode se tornar um vetor unidimensional com número par de elementos ")
else:
    print("Pode se tornar um vetor unidimensional com número ímpar de elementos ")

#Exercício 5
np.random.seed(10) #Padroniza os números aleatórios
mtz = np.random.randint(1, 51, [4,4] )
print(mtz) #matriz 4x4

# Média de cada linha e cada coluna
media_linha = np.mean(mtz, axis=1)
media_coluna = np.mean(mtz, axis=0)
print("Média das linhas: ", media_linha)
print("Média das colunas: ", media_coluna)

# O maior valor das médias
maior_valorL = np.max(media_linha)
maior_valorC = np.max(media_coluna)
print("Maior valor da média das linhas: ", maior_valorL)
print("Maior valor da média das colunas: ", maior_valorC)

# Mostra os números únicos do array
print(np.unique(mtz))

# Quantidade de vezes que aparece
numero, quantidade = np.unique(mtz, return_counts=True)

for c in range(len(numero)):
    if quantidade[c] == 2:
        print("Números que aparecem 2 vezes: ", numero[c])