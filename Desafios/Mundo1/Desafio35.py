print('======DESCRUBRA SE COM AS MEDIDAS INFORMADAS FORMAM UM TRIANGULO======')
m1 = float(input('Digite a primeira medida: '))
m2 = float(input('Digite a segunda medida: '))
m3 = float(input('Digite a terceira medida: '))
#l = [m1, m2, m3]
if m1 < m2 + m3 and m2 < m1 + m3 and m3 < m1 + m2:
    print('Os seguimentos acima podem formar um triângulo')
else:
   print('Os seguimentos acima não formam um triângulo')


