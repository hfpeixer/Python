soma = 0
count = 0 #variavel para contar quantos números ele encontrou
#range(inicia, até, pulando) inícia em 1 e terminha e 501, pulando 2 em 2
#pegando somente os números ímpar
for c in range(1, 501, 2):
    if c % 3 == 0:
        count += +1
        soma += c
print('A soma dos números {} números ímpares de 1 à 501 é {}'.format(count, soma))
print('A quantidade de números somados foram {}'.format(count) )
