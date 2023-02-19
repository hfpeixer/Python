#formula TERMO GERAL DA PROGRESSÃO ARITMÉTICA
'''' an = a1 + (n -1) * r
an = termo que queremos descobrir
a1 = primeiro termo da progressão
n = posição do termo que queremos descobrir
r = razão > sucessor - antecessor
'''
primeiro_termo = int(input("Digite o primeiro termo: ")) # Solicita ao usuário o primeiro termo e a razão da PA
razao = int(input("Digite a razão: "))
#quantidade_termos = int(input("Digite a quantidade termos: ")) # Solicita ao usuário a quantidade de termos da PA
termo = primeiro_termo # Inicializa a variável que armazenará o valor do termo atual
contador = 1 # Inicializa a variável de contagem
total = 0
inicial = 10

# Loop que imprime os termos da PA e exibe um menu ao final da quantidade de termos
while inicial != 0:
    total = total + inicial
    while contador <= total:
        print('{} ->'.format(termo), end='')
        termo += razao
        contador += 1
    print('pausa')
    inicial = int(input('Quantos termos você quer mostrar mais? '))
print('Finalizado')








