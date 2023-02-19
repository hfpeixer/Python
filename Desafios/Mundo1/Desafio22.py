nome =  str(input('Digite o seu nome: ')).strip()
#maisculos
print ('Seu nome em maiúsculo é: ', nome.upper())
#minusculo
print ('Seu nome em minúsculo é: ', nome.lower())
#qtdade de espaços
espacos = nome.count(' ')
#total de letras
total = len(nome)
#qts letras ao todo sem contar os espaços
print('Seu nome tem ao todo: {} letras'.format(total - espacos))
#lista
lista = nome.split()
#qtas letras primeiro nome
#opcao 1
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#opcao 2
print('Seu primeiro nome é {} em tem {} letras '.format(lista[0] , len(lista[0])))

