from datetime import date
cores = {'vm' : '\033[7:31m',
                  'limpa' : '\033[m'}
linhas = '-' * 20
anoatual = date.today().year
print(linhas, 'Prazo de Alistamento', linhas)
ano = int(input('Informe seu ano de nascimento: '))
idade = (anoatual - ano)
if idade > 18:
    print('Corra logo, já se passaram {}{}{} anos para seu alistamento!'.format(cores['vm'], idade-18, cores['limpa']))
elif idade == 18:
    print('Está na hora, procure a unidade militar mais proxíma e aliste-se!')
else:
    print('Fique ligado, faltam {} anos para você se apresentar!'.format((idade-18)*-1))






