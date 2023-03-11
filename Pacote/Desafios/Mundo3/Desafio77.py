t = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
print(t)
for l in t:
    # print cada palavra
    print(f'\nNa palavra {l.upper()} temos ', end='')
    # procura cada vogal dentro da palavra no FOR
    for vogal in l:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
