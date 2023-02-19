print('=' * 20)
print('Sequência Fibonacci')
print('=' * 20)
qtdade = int(input('-> Quantos elementos você quer saber: '))
elemento1 = 0
contador = 1
elemento = 2
print(elemento1)
while contador <= qtdade:
    elemento = elemento1 + contador
    print(elemento)
    elemento1 = contador
    contador = elemento
    contador += 1
    
print('fim')
