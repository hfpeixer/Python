num = int(input('Digite um número entre 0 e 9999: '))
unidades = num // 1 % 10
dezenas = num // 10 % 10
centenas = num // 100 % 10
milhar  = num // 1000 % 100
print ('Unidades: {}\n Dezenas: {}\n Centenas: {}\n Milhar: {}'.format(unidades, dezenas, centenas, milhar))
