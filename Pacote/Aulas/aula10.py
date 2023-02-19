tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro Novo')
else:
        print('Carro Velho')
print('===Fim===')

nome = str(input('Qual seu nome? ')).strip()
if nome.capitalize() == 'Hewerson':
   print('Que nome lindo você tem!')
print('Bom dia, {}!'.format(nome.capitalize()))
print('===Fim===')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print('Sua média foi {:.1f}'.format(m))
if m >=6:
    print('Você está na média, continue assim!')
else:
    print('Você está abaixo da média estude mais!')



