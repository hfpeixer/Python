nome = str(input('Digite seu nome completo: ')).strip()
print('Prazer em te conhecer!')
#split cria lista
lista = nome.split()
print(lista)
print('Seu primeiro nome é {}'.format(lista[0]))
print('Seu último nome é {}'.format((lista[len(lista)-1])))



