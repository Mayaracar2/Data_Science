import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str',  encoding='latin1')

#================Exercício 1=====================
#Extraindo as colunas do dataset
print(dataset[0,:])

#Coluna das missões
print(dataset[:,7])

#Quantas missões existem
total = len(dataset[1:, 7]) #Não inclue o cabeçalho
print(total)

#Quantas deram certo
sucesso = np.sum(dataset[1:,7] == 'Success')
print(sucesso)

#Extraindo a porcentagem
porcentagem = round((sucesso/total)*100,2)
print('Porcentagem de sucesso: ', porcentagem, '%')

#===================Exercício 2===================
#Coluna do custo
print(dataset[1:, 6])

#Transformando em float
custos = dataset[1:, 6].astype(float)

#Custos maiores que zero
maiores = custos[custos > 0]

#Cálculo da média
media = np.mean(maiores)
print('Média dos custos maiores que zero: ', round(media,2))

#==================Exercício 3======================
#Coluna das localizações
print(np.unique(dataset[1:, 2])) #unique foi usado para ver todos, já que eu não estava tendo retorno com EUA

#Quantidade de missões feitas pelo EUA)
USA = np.sum((np.char.endswith(dataset[1:, 2], 'USA'))) #end pois sempre está no final da frase = "termina com"
print(USA)

#=================Exercício 4=======================
#Coluna das empresas
empresas = dataset[1:, 1]

#Missões
missoes = dataset[1:, 4]

#Pegar somente os custos da SpaceX
custos_spacex = custos[empresas == 'SpaceX']

#Encontrar o maior valor
maior_custo = np.max(custos_spacex)

#Missão correspondente
missao = missoes[(empresas == "SpaceX") & (custos == maior_custo)]

print('Maior custo da SpaceX: ', maior_custo)
print('Missão: ', missao)

#=================Exercício 5=======================
#Coluna das empresas
empresas = dataset[1:, 1]

#Quantidade de empresa e quantidade de missões
empresas_unicas, quantidades = np.unique(empresas, return_counts=True)

#Mostrando as informações juntas com for
for empresa, quantidade in zip(empresas_unicas, quantidades):
    print('A empresa ',empresa,'tem ', quantidade, ' de missões')