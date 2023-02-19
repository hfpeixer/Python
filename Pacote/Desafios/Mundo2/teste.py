primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
#totaltermos = 10
termo = 1
contator = False
#menu = int(input('Escolha uma opção:\n[1] Mais termos\n[2] Sair'))

while not contator:
    an = primeirotermo + (termo - 1) * razao
    print(an, '-> ' if termo < 11 else '', end='')
    termo +=1
    if termo >= 11:
        contator = True
    elif contator == True:
            print(int(input('Escolha uma opção:\n[1] Mais termos\n[2] Sair')))
