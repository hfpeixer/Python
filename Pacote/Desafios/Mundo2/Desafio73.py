times = 'Corinthians', 'Palmeiras', 'Santos', 'Flamengo', 'Inter', 'Gremio', 'São Paulo', 'Atlético Mineiro', 'Atlético Paranaense', 'Cruzeiro', 'Botafogo', 'Bahia', 'Fluminense', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América Mineiro', 'Vitória', 'Paraná'
time2 = 'Chapecoense'
print(f'Os cincos primeiros times são: {times[:5]}')
print('=' * 10)
print(f'Os últimos quatro colocados são: {times[-4:]}')
print('=' * 10)
print(f'Em Ordem alfabética: {sorted(times)}')
print('=' * 10)
print(f'O time da Chapeconense está na {times.index(time2)+1} posição')
