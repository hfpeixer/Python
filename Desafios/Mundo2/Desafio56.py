media = 0
menor20 = 0

idade = 0

velhohomem = 0
novamulher = 0
nomevelho = ''

for s in range(1, 5):
    print('----- {} PESSOA -----'.format(s))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip()
    media += idade
    if s == 1 and sexo in 'Mm':
        velhohomem = idade
        nomevelho = nome
    
    if s == 1 and sexo in 'Ff':
        menor20 += 1
       
    if idade > velhohomem:
        velhohomem = idade
        nomevelho = nome
       
    if idade < 20 and sexo in 'Ff':
        menor20 += 1
mediaidade = media / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} e se chama {}.'.format(velhohomem, nomevelho))
print('E temos {} pessoas do sexo Feminino menores de 20 anos'.format(menor20))