import time

c = 10
print('Iniciando a contagem regressiva!')
while c >= 0:
    print(f' Contando... \n {c}')
    c -= 1
    if c == 0:
        break
    time.sleep(1)
print('BOOM')


