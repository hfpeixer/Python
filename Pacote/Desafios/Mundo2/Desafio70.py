print('=' * 15, 'LOJA QUERO MAIS', '=' * 15)
total = 0
mais_1000 = 0
nome_mais_barato = ''
menor = 0
while True:
    produto = str(input('Digite o nome do produto: ')).strip().upper()
    preco = int(input('Digite o preço: R$ '))
    total += preco
    if menor == 0:
        menor = preco
    if preco > 1000:
        mais_1000 += 1
    elif preco < menor:
        menor = preco
        nome_mais_barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'O total da compra foi R$ {total:.2f}')
print(f'Temos {mais_1000} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {nome_mais_barato} que custa R$ {menor:.2f}')
