from random import randint
from time import sleep
computador = randint(0, 10)
print(computador)
acertou = False
contador = 0
print('Será que você vai acertar!')
sleep(1)
while not acertou:
    jogador = int(input('Qual número eu pensei? '))
    contador += 1
    if jogador == computador:
        acertou = True
        
print('Você precisou de {} tentativas para acertar o número que pensei que foi {}'.format(contador, computador))
