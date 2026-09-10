#Criação da minha lista
musicas = []

while True:
    #Criação do dicionário
    musica = {}

    musica["Nome"] = input("Digite o nome do musica: ")
    musica["Ano"] = input("Digite o ano da musica: ")

    musicas.append(musica)  #Adiciona no final

    continuar = input("Deseja continuar? [S/N]").upper()

    if continuar == "N":
        break

print(musicas)

#Fazendo a leitura da quantidade
print("Quantidade de musicas cadastradas: ", len(musicas))

#Encontrando o ano mais antigo
anos = []

for musica in musicas:
    anos.append(musica["Ano"])

ano_mais_antigo = min(anos)

print("Música com ano mais antigo:")

for musica in musicas:
    if musica["Ano"] == ano_mais_antigo:
        print(musica)

