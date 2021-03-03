colocados = ('Flamengo', 'Internacional', 'Atlético - MG', 'São Paulo', 'Fluminense',
                      'Grêmio', 'Palmeiras', 'Santos', 'Atlético - PR', 'Bragantino', 'Ceará - SC', 'Corinthians',
                      'Atlético - GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama', 'Goiás', 'Coritiba',
                      'Botafogo')

print(f'Os cinco primeiros colocados foram: {colocados[0: 5]}')
print(f'Os quatro últimos colocados foram: {colocados[16:20]}')
print(f'Times em ordem alfabética {sorted(colocados)}')
print(f'O time da Fortaleza está na posição {colocados.index("Fortaleza")}')
