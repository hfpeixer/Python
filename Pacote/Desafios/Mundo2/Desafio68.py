from random import randint

perdedor = False
cont = 0
print('-=' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-=' * 15)
while True:
    computador = randint(0, 10)
    jogador = int(input('Faça sua jogada: '))
    print('-=' * 15)
    soma = jogador + computador
    escolha = ' '
    while escolha not in 'PI':  # valida as entradas, enquanto for valor diferente não vai avançar
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
        if escolha == 'P' and soma % 2 == 0:
            vencedor = 'PAR'
            print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {vencedor}')
            print('Você venceu!!!')

        elif escolha == 'I' and soma % 2 == 1:
            vencedor = 'ÍMPAR'
            print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {vencedor}')
            print('Você venceu!!!')
        else:
            if soma % 2 == 0:
                vencedor = 'PAR'
            else:
                vencedor = 'ÍMPAR'
                print(f'Você jogou {jogador} e o computador {computador}. Total deu {soma} DEU {vencedor}')
                print(f'Você teve {cont} vitórias') 
                print('Você perdeu!!!')
            perdedor = True
        cont += 1
    if perdedor:
        break

