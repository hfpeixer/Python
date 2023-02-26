maior_18 = 0
masculino = 0
mulheres_menores_20 = 0
while True:
    idade = int(input('Qual a idade: '))
    if idade > 18:
        maior_18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual o sexo [M/F]: ')).strip().upper()[0]
        if sexo == 'M':
            masculino += 1
            print(masculino)
        elif idade < 20 and sexo == 'F':
            mulheres_menores_20 += 1
            print(mulheres_menores_20)
    continuar = ' '
    while continuar not in 'SN':    
        continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print ('=' * 5, 'FIM DO PROGRAMA', '=' * 5)
print (f'Total de pessoas com mais de 18 anos: {maior_18}')
print (f'Ao todo temos {masculino} homens cadastrados')
print (f'E temos {mulheres_menores_20} mulheres com menos de 20 anos')