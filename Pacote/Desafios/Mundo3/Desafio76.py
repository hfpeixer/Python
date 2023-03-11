t = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90 )
linha = '#' * 50
total = len(t)
primeiro = 0
segundo = 2
print(linha)
print(f'{"LISTAGEM DE PREÇOS":^50}')
print(linha)
for lista in range(0, total):
    # a posição dos produtos são pares, assim imprime somente eles
    if lista % 2 == 0:
        print(f'{t[lista]:.<40}', end='')
    else:
        print(f'R${t[lista]:>8.2f}')
print(linha)

