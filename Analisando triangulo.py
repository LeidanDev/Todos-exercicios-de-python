a = float(input('Digite o primeiro valor: '))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
# c < a + b
if a < b + c and b < a + c and c < a + b:
    print(f'Os valores  formam um triangulo')
else:
    print('Os valores não formam um triangulo')