n = int(input('Digite um número: '))
media = 0
maior = n
menor = n
soma = n
cont = 1
parar = False
while not parar:
    print('=' *20)
    n = int(input('Deseja parar? \n[1] SIM\n[2] NÃO\n>>> '))
    if n == 1:
        parar = True
        print('=' * 20)
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        soma = soma + n
        media = soma / cont
    #cont += 1     
    else:
        print('=' * 20)
        n = int(input('Digite um número: '))
        soma = soma + n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        cont += 1
        media = soma / cont    
        
        
print('A quantidade de números digitados foi {}, com as seguites dados:\nMenor valor > {}\nMaior Valor > {}\nSoma de > {}\nMédia de > {:.2f}'.format(cont, menor, maior, soma, media))
        