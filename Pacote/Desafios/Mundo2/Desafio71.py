print('=' * 15, 'CAIXA ELETRÔNICO', '=' * 15)


saque = int(input('Qual o valor do saque? R$ '))
milhar = saque // 50
milhar_total = saque // 50 * 50
sobra = saque - milhar_total

centena = sobra // 20
centena_total = centena * 20
sobra -= centena_total
#print(f'Centena_total {centena_total}')

dezena = sobra // 10
dezena_total = dezena * 10
sobra -= dezena_total
#print(f'dezena_total {dezena_total}')

unidade = sobra // 1

if milhar != 0:
    print(f'Total de {milhar:.0f} cédula de R$ 50')
if centena != 0:
    print(f'Total de {centena:.0f} cédula de R$ 20')
if dezena != 0:
    print(f'Total de {dezena:.0f} cédula de R$ 10')
if unidade != 0:
    print(f'Total de {unidade:.0f} cédula de R$ 1')


