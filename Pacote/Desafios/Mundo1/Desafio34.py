s = int(input('Qual o valor do salário? '))
if s <= 1250:
    print('O seu salário será reajustado  em 15%, passando a totalizar R${:.2f}'.format((s*15)/100+s))
else:
    print('O seu salário será reajustado  em 10%, passando a totalizar R${:.2f}'.format((s*10)/100+s))