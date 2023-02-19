menor = 0
maior = 0
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª: '.format(p)))
    if p == 1: # menor e maior assumem os primeiros dados inseridos
        menor = peso
        maior = peso
    else:
        if menor > peso:
            menor = peso
        if maior < peso:
            maior = peso
print('O menor peso foi {} kg'.format(menor))
print('O maior peso foi {} kg'.format(maior))
  