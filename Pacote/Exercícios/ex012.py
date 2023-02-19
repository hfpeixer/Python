p = float(input('Digite o valor do produto: '))
d = float(input('Digite o desconto: '))
pf = p - (p*d/100)
print('O valor com desconto ficou R${:.2f}'.format(pf))