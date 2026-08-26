from ast import literal_eval

import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype='str',  encoding='latin1')

#=====================Questão 1=====================
#Mostrando as colunas
print(dataset[0,:])

print("===============Questão 1==================")

#Mostrando as colunas específicas
print(dataset[:,:4])

#====================Questão 2=====================

print("===============Questão 2====================")

#Coluna da região
regioes = dataset[1:,1]

#Diferentes regioes
diferentes, quat = np.unique(regioes, return_counts=True)

#Mostrando os nomes
print(diferentes)

#Quantidades de regioes
print("Quantidade de regiões: ", (len(quat)))

#======================Exercício 3========================
print("===============Questão 3====================")

#Mostrando a media da coluna literacy
literacy = round(np.mean(dataset[1:,9].astype(float)),2)

print("Taxa média de alfabetização do planeta: " , literacy)

#=======================Exercício 4=======================

print("===============Questão 4====================")

#Encontrando quantos Américas do Norte aparecem
Northern_America = np.sum(np.char.find(dataset[1:, 1], "NORTHERN AMERICA")>=0)

print("Quantidade de países na América do Norte: ", Northern_America)

#========================Exercício 5========================

print("===============Questão 5====================")

#Países da AL e CARIBE
filtro = np.char.find(dataset[1:, 1], "LATIN AMER. & CARIB") >= 0
AL_C = dataset[1:][filtro]
print(AL_C)

#Maior gdp
renda = AL_C[:,8].astype(float)

Maior_renda = np.argmax(renda)

pais = AL_C[Maior_renda,0]
print("País da América do Sul e Caribe com a maior renda per capita: ", pais)









