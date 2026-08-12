#Exercício 4
nomes = []
pesos = []

for c in range(3):
    nome = (input('Digite seu nome: '))
    peso = (int(input('Digite seu peso: ')))

    nomes.append(nome)
    pesos.append(peso)

pesado = max(pesos)
leve = min(pesos)

mais_leve = pesos.index(leve)
mais_pesado = pesos.index(pesado)

print("A pessoa mais leve é ", nomes[mais_leve])
print("A pessoa mais pesada é ", nomes[mais_pesado])

#Exercício 5
nomes = []
idades = []
sexos = []
n = (int(input("Quantas pessoas deseja registrar? ")))

for c in range(n):
    nome = (input('Digite seu nome: '))
    idade = (int(input('Digite sua idade: ')))
    sexo = (input('Digite seu sexo: '))

    #append como o valor digitado como o último da fila
    nomes.append(nome)
    idades.append(idade)
    sexos.append(sexo)

soma_idade = sum(idades)
media_idade = soma_idade /n
print("A média das idades é: ", round(media_idade, 2))

quantidade = 0
for c in range(n):
    if idades[c] < 20 and (sexos[c] == 'F' or sexos[c] == 'f') :
        quantidade += 1

print("Quantidade de mulheres com menos de 20 anos: ", quantidade)

#Exercício 6
ingredientes = ['farinha', 'ovo', 'achocolatado', 'óleo', 'açúcar', 'fermento']

ingredientes.append('manteiga') #adiciona no final da fila
print(ingredientes)

ingredientes.insert(3, 'baunilha')
print(ingredientes)

ingredientes.remove('achocolatado')
print(ingredientes)






