#formula TERMO GERAL DA PROGRESSÃO ARITMÉTICA
'''' an = a1 + (n -1) * r
an = termo que queremos descobrir
a1 = primeiro termo da progressão
n = posição do termo que queremos descobrir
r = razão > sucessor - antecessor
'''
primeirotermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
an = primeirotermo + (10 - 1) * razao
for c in range(primeirotermo, an + 1, razao):
    print(' ->', c, end='')
print()
