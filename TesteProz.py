rodas = int(input('Digite a quantidade de rodas: '))
pessoa = int(input('Digite a quantidade de pessoas: '))
peso = int(input('Digite a quantidade de peso: '))

if (pessoa <= 2) and (rodas <= 3) and (peso != 0):
    print('Você precisa de um veículo categoria A')
elif (rodas <= 4) and (pessoa >= 1 <= 8) and (peso <= 3500):
    print('Você precisa de um veículo categoria B')
elif (rodas >= 4) and  (pessoa <= 8) and (peso >3500 and peso <6000):
    print('Você precisa de um veículo categoria C')
elif (rodas >= 4) and (pessoa >= 8) and (peso <= 6000):
    print('VocÊ precisa de um veículo categoria D')
else:
    print('Você precisa de um veículo categoria E')
