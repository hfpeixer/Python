nome = str(input('Digite seu nome completo: ')).strip().title()
print(nome)
#opcao1
print('Seu nome tem a palavra Silva? {}'.format('Silva' in nome))
#opcao2
print('Seu nome tem a palavra Silva? {}'.format('silva' in nome.lower()))