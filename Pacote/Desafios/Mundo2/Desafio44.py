linhas = '-' * 20
print(linhas, 'Calculadora de Caixa', linhas)
preco = float(input('Informe o valor do produto: R$ '))
condicao = int(input('Informe a condição de pagamento '
                     '\n Digite 1 para "À Vista"'
                     '\n Digite 2 para "À Vista Cartão"'
                     '\n Digite 3 para "2X Cartão" '
                     '\n Digite 4 para "3X ou mais" \n Qual opção você escolheu: '))
av = 0.10
avc = 0.05
tresvx = 0.20
if condicao == 1:
    print('À vista você ganha 10% de desconto, preço final R${:.2f}'.format(preco - (preco*av)))
elif condicao == 2:
    print('À vista no cartão você ganha 5% de desconto, preço final R${:.2f}'.format(preco - (preco*avc)))
elif condicao == 3:
    print('Em 2x no  cartão, preço final R${:.2f}'.format(preco))
else:
    print('Em 3x ou mais no  cartão terá um acréscimo de 20% , preço final R${:.2f}'.format(preco + (preco*tresvx)))