from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os números sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO menor valor sorteado é {min(numeros)}')
print(f'O maior valor sorteado foi {max(numeros)}')
print(type(numeros))
