from datetime import date
if a == 0:
    a = date.today().year # pega o ano atual da máquina
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 :
     print('O ano informado {} é BISSEXTO'.format(a))
else:
    print('O ano informado {} não é BISSEXTO'.format(a))

