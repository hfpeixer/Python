n = str(input('Digite algo?: '))

print('O tipo primitivo', n)
print('O tipo primitivon deste valor é', type(n))
print('Só tem espaços?', n.isspace())
print('É número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanumérico?', n.isalnum())
print('Está em maiúcula?', n.isupper())
print('Está em minúcula?', n.islower())
print('Está em capitalizada', n.istitle())
