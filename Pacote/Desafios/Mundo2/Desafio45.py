linhas = '-' * 20
print(linhas, 'Jogo Jokenpô', linhas)
from random import choice
from time import sleep
lista = ['PEDRA', 'PAPEL', 'TESOURA']
computador = choice(lista)
print('Adversário Jogou = *******')
jogador = str(input('Sua vez de jogar: ')).upper()
linhas = '-' * 20
print('Jo')
sleep(1)
print('ken')
sleep(1)
print('pô')
sleep(.5)

if computador == 'PEDRA' and jogador != 'PAPEL' and jogador != 'PEDRA':
    print('Você perdeu o adversário jogou {}'.format(computador))
elif computador == 'PAPEL' and jogador != 'TESOURA' and jogador != 'PAPEL':
   print('Você perdeu o adversário jogou {}'.format(computador))
elif computador == 'TESOURA' and jogador != 'PEDRA' and jogador != 'TESOURA':
   print('Você perdeu o adversário jogou {}'.format(computador))
elif computador == jogador:
  print('Empate, o adversário jogou {}'.format(computador))
else:
    print('Parábens, você ganhou!!!, o adversário jogou {}'.format(computador))
