#Exercício 7
ingredientes = ['farinha', 'ovo', 'achocolatado', 'óleo', 'açúcar', 'fermento']
pessoa1 = {'farinha', 'óleo', 'açúcar'}
pessoa2 = {'farinha', 'ovo', 'fermento', 'óleo'}

#set(ingredientes) -> transforma a lista em um conjunto

falta_pessoa1 = set(ingredientes) - pessoa1
print("A pessoa 1 precisa comprar: ", falta_pessoa1)

falta_pessoa2 = set(ingredientes) - pessoa2
print("A pessoa 2 precisa comprar: ", falta_pessoa2)

#Exercício 8
mercado = []
estoque = []

for c in range(3):
    nome = (input("Digite o nome do produto: "))
    preco = (float(input("Qual o preço? ")))
    quantidade = (int(input("Digite o quantidade de produto no estoque: ")))

    produtos = {"Nome": nome,
                 "Preço": preco,
                "Quantidade em estoque": quantidade}

    valor_estoque = preco * quantidade

    mercado.append(produtos)
    estoque.append(valor_estoque)

for c in range(len(mercado)):
    print("Produto:", mercado[c]["Nome"], "Valor total em estoque: ", estoque[c])

