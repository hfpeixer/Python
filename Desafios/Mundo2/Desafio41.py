from datetime import date
anoatual = date.today().year
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = anoatual - ano

if idade <=9:
    print('A categoria deste atleta é {}'.format('MIRIM'))
elif idade  <=14:
    print('A categoria deste atleta é {}'.format('INFANTIL'))
elif idade <=19:
    print('A categoria deste atleta é {}'.format('JUNIOR'))
elif idade <=25:
    print('A categoria deste atleta é {}'.format('SÊNIOR'))
else:
   print('A categoria deste atleta é {}'.format('MASTER'))
