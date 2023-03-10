a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais número: '))
d = int(input('Digite o último número: '))
t = (a, b, c, d)


print(f'O número 9 apareceu {t.count(9)} vezes')
if 3 in t:
    print(f'O primeiro número 3 informado foi na posição {t.index(3)+1}')
else:
    print(f'O número 3 não apareceu em nunhuma posição')
print('Os valores pares foram ', end='')
for p in t:
    if p % 2 == 0:
        print(p, end=' ')