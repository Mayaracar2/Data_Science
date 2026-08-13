#Exercício 1
import numpy as np

arr1 = np.ones(8)
#print(arr1)

arr2 = np.random.randint(1, 10, 8 )
#print(arr2)

arr3 = arr1 + arr2
#print(arr3)

soma = arr3.sum()
if (soma >= 40):
    print(arr3.reshape(4,2))
else:
    print(arr3.reshape(2,4))

#Exercício 2
arr1 = np.arange(0,51,2)
arr2 = np.arange(100,50,-2)

arr3 = np.concatenate([arr1,arr2])
ordenado = np.sort(arr3) #Reordena o próprio array
print(ordenado)

#Exercício 3
contador = 0
mtz = np.zeros([2,2]) #matriz criada

#Sortear a posição do 1
linha_mina = np.random.randint(0,2)
coluna_mina = np.random.randint(0,2)
mtz[linha_mina][coluna_mina] = 1

while(contador != 3):
  linha = int(input("Qual linha deseja escolher? "))
  coluna = int(input("Qual coluna deseja escolher? "))

  if(mtz[linha][coluna] == 1):
    print('Game Over! Try again!')
    break
  else:
    contador += 1

if(contador == 3):
    print('Congratulations! You beat the game')



