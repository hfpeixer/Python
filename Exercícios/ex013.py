s = float(input('Digite o salário do funcinário: R$ '))
a = float(input('Porcentagem de aumento: '))
sf = s + (s*a/100)
print('O salário com {:.0f}% de aumento fica R${:.2f}'.format(a,sf))
