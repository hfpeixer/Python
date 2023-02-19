print('-=-' *10)
print('CÁLCULADORA DE TABUADA')
print('-=-' *10)


numero = int(input('Qual a tabuada você deseja:  '))
for c in range(1, 11):
    resultado = c*numero
    print('{} X {} = {}'.format(numero, c, resultado))
