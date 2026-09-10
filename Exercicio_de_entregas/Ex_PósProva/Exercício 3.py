import numpy as np

colors = [
    {"color": "black", "type": "primary", "code": {"rgba": [255,255,255,1], "hex": "#000"}},
    {"color": "green", "type": "secondary", "code": {"rgba": [0,255,0,0.1], "hex": "#0F0"}},
    {"color": "yellow", "type": "primary", "code": {"rgba": [255,255,0,0.7], "hex": "#FF0"}},
    {"color": "blue", "type": "primary", "code": {"rgba": [0,0,255,1], "hex": "#00F"}}
]

#Mostrar as cores que são primárias
for cor in colors:
    if cor["type"] == "primary":
        print(cor["color"])

#Cores com azul máximo
for cor in colors:
    if cor["code"]["rgba"][2] == 255:
        print(cor["code"]["hex"])

#Criar um NumPy Array 1-D
dados = []

for cor in colors:
    dados.append(cor["color"])
    dados.append(cor["code"]["hex"])

array = np.array(dados)
print(array)

#Transformar em Array 2-D
array = np.reshape(array, (4,2))
print(array)

#Trocar os nomes para português
array[0,0] = "preto"
array[1,0] = "verde"
array[2,0] = "amarelo"
array[3,0] = "azul"

print(array)