from math import sqrt, hypot
adj = float(input('Digite o comprimento do lado adjacente: '))
oposto = float(input('Digite o comprimento do lado oposto: '))
print (sqrt(adj*adj + oposto*oposto))

hi = hypot(adj, oposto)

print(hi)
