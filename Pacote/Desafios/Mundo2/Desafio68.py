from random import randint
perdedor = False
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
while True:
    computador = randint(1, 10)
    #print(computador)
    jogador = int(input('Faça sua jogada: '))
    escolha = str(input('Par ou Ímpar? [P/I] ')).upper()
    soma = jogador + computador
    if escolha == 'P' and soma % 2 == 0:
        vencedor = 'PAR'
        print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {vencedor}')
        print('Você venceu!!!')
        print('-=' * 15)
    elif escolha == 'I' and soma % 3 == 0:
        vencedor = 'ÍMPAR'
        print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {vencedor}')
        print('Você venceu!!!')
        print('-=' * 15)
    else:
        if soma % 2 == 0:
            vencedor = 'PAR'
        else:
            vencedor = 'ÍMPAR'
        print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {vencedor}')
        print('Você perdeu!!!')
        perdedor = True
    if perdedor == True:
        break

