#Exercício 4
distancia = int(input('Qual a distância da viagem em km ?'))

if distancia <= 200:
    print('Valor da passagem: ', distancia * 0.5)
else:
    print('Valor da passagem: ', distancia * 0.45)

#Exercício 5
numero = int(input('Digite um valor entre 1000 até 9999'))
while numero < 1000 or numero > 9999:
    numero = int(input('Digite um valor entre 1000 até 9999'))

numero = str(numero)

print('O número da unidade é: ', numero[3])
print('O número da dezena é: ', numero[2])
print('O número da centena é: ', numero[1])
print('O número do milhar é: ', numero[0])

#Exercício 6
import math

Numero = float(input('Digite um número decimal: '))

print('Raiz: ', math.sqrt(Numero))
print( 'Função teto: ', math.ceil(Numero))
print( 'Função chão: ', math.floor(Numero))
print('Número inteiro: ', math.trunc(Numero))
