#Exercício 1
nome = ['Flamengo', 'Santos', 'Barcelona', 'São Paulo', 'Palmeiras']
print(nome)
print(type(nome))

print(nome[0:3])
print(nome[3:5])

times_ordenados = sorted(nome) ## função organiza os itens e retorna uma nova lista sem alterar e 'o sort ' é o método que reogarniza a lista em ordem alfabética
print(times_ordenados)

posicao = nome.index('Barcelona')
print(posicao)

#Exercício 2
lojaA = {'Iphone 17', 'J5 prime', 'MotoG4', 'Nokia'}
lojaB = {'Iphone 17', 'A35', 'Xiaomi 10'}

total_marcas = lojaA | lojaB
print(total_marcas)

disponivel_ambas = lojaA & lojaB
print(disponivel_ambas)

#Exercício 3
nome = (input("Digite seu nome: "))
media = (int(input("Digite sua média: ")))

aluno = {'Nome': nome,
'Média': media}

if(media >= 50):
    situacao = 'AP'
else:
    situacao = 'RP'

print("Situação escolar: ", situacao )