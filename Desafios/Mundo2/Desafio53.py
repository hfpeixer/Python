'''Como descobrir se uma palavra é um PALÍNDROMO
palavra = str(input('Digite a palavra desejada: ')).strip().upper() #strip tira os espacos do inicio e fim / upper tudo em maiusculo
lista = palavra.split() #split cria uma lista com a frase informada
junto = ''.join(lista) #join juntando o que esta em '' com a lista
inverso = '' #apenas declarando a variavel que está vazia por enquanto
for s in range(len(junto)-1, -1, -1): #ranger(inicio, fim, ordem - se for negativa é para decrescente)
   inverso += junto[s] #inverso que era vazio passa a receber do for
if inverso == junto:
    print('A frase escolhida é um PALÍNDROMO')sd
else:
    print('A frase escolhida não é um PALÍNDROMO')'''

'''OPCAO SEM O FOR'''
palavra = str(input('Digite a palavra desejada: ')).strip().upper() #strip tira os espacos do inicio e fim / upper tudo em maiusculo
lista = palavra.split() #split cria uma lista com a frase informada
junto = ''.join(lista) #join juntando o que esta em '' com a lista
inverso = junto[::-1]
if inverso == junto:
    print('A frase escolhida é {} e de de trás pra frente {} um PALÍNDROMO'.format(junto, inverso))
else:
    print('A frase escolhida é {} e de de trás pra frente {} não é um PALÍNDROMO'.format(junto, inverso))
