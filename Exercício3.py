#Exercício 7
palavra = input('Digite uma palavra: ')
quantidade_vogais = 0
tem_A = False

for letra in palavra:
    print(letra.upper())
    print()

    if letra.lower() == 'a' or letra.lower() == 'e' or letra.lower() == 'i' or letra.lower() == 'o' or letra.lower() == 'u':
        quantidade_vogais += 1

    if letra == 'a' or letra == 'A':
        tem_A = True

print( 'Quantidade de vogais: ', quantidade_vogais )

if tem_A == True:
    print( 'Tem A')
else:
    print('Não tem A')

#Exercício 8
Num1 = float(input('Digite um número: '))
Num2 = float(input('Digite outro número: '))

print('Adição: ', Num1 + Num2)
print('Subtração: ', Num1 - Num2)
print('Multiplicação: ', Num1 * Num2)
print('Divisão: ', Num1 / Num2)
print('Resto da divisão: ', Num1 % Num2)
print('Potência: ', Num1 ** Num2)
