t = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatrorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número de 0 à 20: '))
    if n >= 0 and n <= 20:
        break
    else:
        n = int(input('Número inválido!!! Digite um número de 0 à 20: '))  
        
print(f'Você digitou o número {t[n]}')
