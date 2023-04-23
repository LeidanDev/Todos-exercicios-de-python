pessoas = int(input('Quantas pessoas são? '))
fumantes = bool(input('Existe algum fumante? '))
animal = bool(input('Algum animal de estimação? '))

if pessoas >= 5:
    print(f'Vocês estão em {pessoas} pessoas e será alocados no primeiro andar')
elif fumantes >= 1 or animal >=1:
    print('você será alocado na área externa')
else:
    print('Você será alocada no salão principal')
