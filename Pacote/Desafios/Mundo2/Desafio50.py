#Soma somente de numeros pares
soma = 0
contador = 0
for c in range(1, 7): #repetir 6x
    numero = int(input('Digite o {} número: '.format(c)))
    if numero % 2 == 0: #verificando se é par
        soma += numero
        contador += 1
print('Você informou {} números pares e a soma foi {}'.format(contador, soma))



