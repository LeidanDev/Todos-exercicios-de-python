num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINARIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print(f'{num} Convertido para BINARIO é igual {bin(num)[2:]}')
elif opção == 2:
    print(f'{num} convertido para OCTAL é igual {oct(num)[2:]}')
elif opção == 3:
    print(f'{num} convertido para HEXADECIMAL é igual {hex(num)[2:]}')
else:
    print('Escolha apenas opções válidas!')