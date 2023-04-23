vel = int(input('Qual é a velocidade do carro? '))
multa = 7
if vel <= 80:
    print('Tenha uma boa viagem!')
else:
    vel > 80
    total = (vel - 80) * multa
    print(f'Multado! Você excedeu o limite de velocidade de  80 km/h \n Você deve pagar R$:{total:.2f} de multa')
    print('Tenha um bom dia e dirija com segurança!')