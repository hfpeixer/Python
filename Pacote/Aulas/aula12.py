nome = str(input('Qual seu nome? ')).strip().title()
if nome == 'Hewerson':
    print('Que nome bonito!')
elif nome == 'Maria' or nome == 'Pedro' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil!')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))
