import numpy as np

dataset = np.loadtxt('space.csv', delimiter=';', dtype='str',  encoding='latin1')

#===================Exercício 6=======================
#Colunas do dataset
print(dataset[0,:])

#Coluna do Status Rocket
print(dataset[1:,5])

#Missões existentes
total = len(dataset[1:,5]) #Sem o cabeçalho

#Quantidade de missões que estão como "StatusRetired
status = np.sum(dataset[1:,5] == "StatusRetired")

#Calculo da porcentagem
porcentagem = round((status/total)*100, 2)
print('Porcentagem de missões com StatusRetired: ', porcentagem, '%')

#===================Exercício 7======================
#Coluna Location
print(dataset[1:,2])

russia = np.sum(np.char.find(dataset[1:,2], "Russia")>=0) #usamos o >=0 pois assim ele tranforma em true e false
print('Missões lançadas a partir de Russia: ', russia)

#==================Exercício 8=======================
#Empresas
empresas = dataset[1:, 1]

#Custos
custos = dataset[1:,6].astype(float)

#Maior custo
maior_custo = np.max(custos)

#Posição do maior custo
posicao = np.argmax(custos)

#Qual empresa está nessa posição
empresa =empresas[posicao]

print('Empresa: ', empresa)
print('Valor da missão mais cara: ', maior_custo)

