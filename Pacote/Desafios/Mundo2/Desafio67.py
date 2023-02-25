cont = 0
while True:
    n = int(input('Qual tabuada você desaja saber: '))
    print('-' * 20)
    if n < 0:
        break
    while True:
        cont += 1
        t = n * cont
        if cont == 11:
            cont = 0
            n = 0
            break
        print(f'{n} X {cont} = {t}')
    print('-' * 20)
print('Programa tabuada finalizado!')
