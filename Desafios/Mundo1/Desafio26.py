#str declarendo que é string
#strip para excluir espaços no inicio e fim da frase
frase = str(input('Digite uma frase: ').strip())
letra = input('Que letra deseja procurar? ').lower()

#lower para colocar todas as letras em minusculo
#count para contar quantas letras
print('A letra {} apareceu {} vezes na frase.'.format(letra, frase.lower().count('a')))

#lower para colocar todas as letras em minusculo
#find procurar a letra desejada
# +1 para somar com find para mostrar posição iniciando com 1
print('A primeira letra {} apareceu na posição {}'.format(letra, frase.lower().find('a')+1))

#lower para colocar todas as letras em minusculo
#rfind procurar a letra desejada iniciando pela direita
print('A última letra {} apareceu na posição {}'.format(letra, frase.lower().rfind('a')+1))
