v = float(input('Digite a velocidade do carro: '))
if v <= 80:
    print('Você passou dentro do limite de velocidade!')
else:
    print('Você excedeu a velocidade em {}km/h\n Sua multa será de R$ 7,00 por Km/h excedido, totalizando R${:.2f} '.format(v-80, (v-80)*7))
