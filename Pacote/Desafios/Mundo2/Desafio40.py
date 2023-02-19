cores = {'vm' : '\033[31m',
                'am' : '\033[33m',
                'az' : '\033[34m',
                'limpa' : '\033[m'}
n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
n3 = float(input('Informe a terceira nota: '))
media = (n1 + n2 + n3)/3
if media < 5:
    print('Notícia triste, você foi {}{}{}'.format(cores['vm'], 'REPROVADO', cores['limpa']))
elif media >=5 and media < 7:
    print('Faltou pouco, você ficou em {}{}{}'.format(cores['am'], 'RECUPERAÇÃO', cores['limpa']))
else:
    print('Parábens, você foi {}{}{}'.format(cores['az'], 'APROVADO', cores['limpa']))


