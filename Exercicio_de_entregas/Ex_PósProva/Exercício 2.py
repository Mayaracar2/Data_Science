import numpy as np

nomes1 = np.array(["Ana", "Carlos", "Joao", "Maria"])
nomes2 = np.array(["Pedro", "Lucas", "Bruna", "Fernanda"])

#Arrays 1-D com os 4 nomes
print(nomes1)
print(nomes2)

#Arrays concatenados
nomes = np.concatenate((nomes1, nomes2))
print(nomes)

#Transformando em 2-D
nomes = np.reshape(nomes, (2,4))
print(nomes)

#Ordem decrescente
nomes = np.sort(nomes.flatten())[::-1].reshape(2, 4)
print(nomes)