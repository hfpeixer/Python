print('=' * 20)
print('Sequência Fibonacci')
print('=' * 20)
qtdade = int(input('-> Quantos elementos você quer saber: '))
elemento1 = 0
elemento2 = 1
contador = 3
print('', elemento1, elemento2, '', end='')
while contador <= qtdade:
    elemento = elemento1 + elemento2
    print(elemento, end=' ')
    elemento1 = elemento2
    elemento2 = elemento
    contador += 1
    
print('fim')
