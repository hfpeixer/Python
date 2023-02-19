'''Descubra se o número é PRIMO'''
n = int(input('Digite um número: '))
total = 0
print('O {} é divisivél por '.format(n))
for c in range(1, n + 1):
    if n % c == 0:
        print(' ->', c, end='')
        t += 1
else:
    if total == 2:
        print('\n O número {} é PRIMO'.format(n))
    else:
        print('\n O número {} não é PRIMO'.format(n))

