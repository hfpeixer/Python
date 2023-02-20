numero = int(input('Digite um número de 1 a 999: '))
soma = numero
cont = 0
continuacao1 = 0
while continuacao1 != 999:
    
    continuacao = soma + continuacao1
    soma = continuacao
    cont += 1
    continuacao1 = int(input('Digite um número de 1 a 999: '))
print('Foram digitado {} números e a soma é de {}'.format(cont, soma))
