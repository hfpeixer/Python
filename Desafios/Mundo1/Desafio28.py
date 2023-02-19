from random import randint # importando a bibliteca randint
from time import sleep
n = randint(0, 5) #randomizando número entre 0 e 5
n1= int(input('Qual número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if n1 == n:
    print('Parábens você acertou!!!')
else:
    print('Que pena você errou!')


