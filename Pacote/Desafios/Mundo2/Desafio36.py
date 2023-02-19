linhas = '-' * 20
print(linhas, 'Simulação de Empréstimos', linhas)
casavl = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual o salário? R$ '))
parcelas = int(input('Em quantas anos vai pagar? '))
vlparcela = casavl/(parcelas*12)
print('{:.2f}'.format(vlparcela))
margem = (salario*30)/100
if vlparcela > margem:
    print('Infezlimente seu empréstimo não foi aprovado!')
else:
    print('Seu empréstimo foi APROVADO!, nas condições de {} parcelas de R${:.2f}'.format(parcelas*12, vlparcela))
