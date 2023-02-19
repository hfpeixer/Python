linhas = '-' * 20
print(linhas, 'Calculadora IMC', linhas)
altura = float(input('Informe sua altura: '))
#peso2 = 25.1*(altura * altura)
#print(peso2)
peso = float(input('Informe seu peso: '))
imc = peso / (altura * altura)
print(imc)
if imc <18.5:
    print('Seu IMC é {:.2f} e está abaixo do Peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é {:.2f} e está com Peso Ideal'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é {:.2f} e está com Sobrepeso'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é {:.2f} e está com Obesidade'.format(imc))
else:
    print('Seu IMC é {:.2f} e está com Obesidade Mórbida'.format(imc))