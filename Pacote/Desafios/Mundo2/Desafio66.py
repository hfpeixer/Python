cont = 0
soma = 0
while True:
    numero = int(input('Digite um número (999 para PARAR: '))
    if numero == 999:
        break
    cont += 1
    soma += numero

print(f'Você digitou {cont} números e a soma deles foi {soma}')
