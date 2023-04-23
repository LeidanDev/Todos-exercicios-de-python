dist = int(input('Qual é a distancia da viagem? '))
val1 = 0.50
val2 = 0.45
total1 = dist * val1
total2 = dist * val2
if dist <= 200:
    print(f'O valor da passagem será R$: {total1:.2f}')
else:
    print(f'O valor da passagem será R$: {total2:.2f}')
