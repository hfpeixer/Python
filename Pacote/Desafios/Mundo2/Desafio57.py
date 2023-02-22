#strip tira os espaços - upper tudo maisculo - [0] lê a primeira letra
sexo = str(input('Digite o sexo: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe o seu SEXO: ')).strip().upper()[0]
print('Cadastro efetuado com sucesso!')
