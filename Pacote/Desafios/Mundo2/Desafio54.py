from datetime import date
anoatual = date.today().year
#ano = int(input('Digite o ano de nascimento: '))
sequencia = 0
maior = 0
menor = 0
for a in range(1, 8):
    ano = int(input('Digite o ano que a {}ª nasceu: '.format(a)))
    idade = anoatual - ano
    if idade >=21:
        maior += 1
    else:
        menor += 1

print('Temos {} MENORES de idade e {} MAIORES de idade'.format(menor, maior))