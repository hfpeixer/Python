from math import factorial
numero = int(input('Digite o número a ser fatorado: '))
fator = numero
n = 1
while fator > 0:# até atingir a condição, vai fazer a sequencia de ações abaixo!
    print(fator, 'X ' if fator > 1 else '= ', end='')
    n *= fator
    fator -= 1
print('{}'.format(factorial(numero)))

   