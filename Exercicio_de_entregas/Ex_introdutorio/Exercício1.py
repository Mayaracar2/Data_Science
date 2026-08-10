#Exercício 1
nome = input('Qual seu nome completo?')

print(nome.upper())
print(nome.lower())
print(len(nome))

vetor = nome.split()
quantidade = len(nome.split())
#print(quantidade)

for c in range(0, quantidade):
    vetor[-1] = "do Inatel"

for N in vetor:
    print(N, end=' ')

print()

#Exercício 2
numero = int(input('Digite qual tabuada você quer saber: '))
inicio = int(input('Da aonde você gostaria de começar?'))
fim = int(input('Até onde você gostaria de ver ?'))

for n in range(inicio, fim+1):
    print(n, 'X', numero, '=', numero * n )

print()

#Exercício 3
sexo = input('Qual seu sexo(M ou F)?')

while sexo != 'M' and sexo != 'F':
    sexo = input('Qual seu sexo(M ou F)?')
    if sexo == 'M' or sexo == 'm':
        print('Homem')
    elif sexo == 'F' or sexo == 'f':
        print('Mulher')
