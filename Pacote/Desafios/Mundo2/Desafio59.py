from time import sleep

linhas = '-=' * 10

valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
print(linhas)
menu = 0
while menu != 5:
    menu = int(input('Escolha uma opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa  '))
    print (linhas)
    if menu == 1:
        somar = valor1 + valor2
        print('Soma dos valores {} e {} é {}'.format(valor1, valor2, somar))
        print(linhas)
    elif menu == 2:
        multiplicar = valor1 * valor2
        print('A multiplicação de {} e {} é {}'.format(valor1, valor2, multiplicar))
        print (linhas)
    elif menu == 3:
        if valor1 > valor2:
            print('O valor maior entre {} e {} é {}'.format(valor1, valor2, valor1))
            print(linhas)
        else:
            print('O valor maior entre {} e {} é {}'.format(valor1, valor2, valor2))
            print(linhas)
    elif menu == 4:
        valor1 = int(input('Digite um valor: '))
        valor2 = int(input('Digite outro valor: ')) 
        print(linhas)
        #valor1 = valor1
        #valor2 = valor2
    elif menu == 5:
        print('Obrigado por usar nossos sistemas!')
    else:
        print('Tente uma opção valida!')
        print(linhas)
        sleep(2)
        

