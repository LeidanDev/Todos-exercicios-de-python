def mostrarNumero():
    try:
        print('Escreva um numero inteiro menor que 100')
        num = int(input())

        if num > 100:
            print('Esse é maior que 100! Digite um número menor que 100')
            return mostrarNumero()
        else:
            print(f'Boa, o número é {num}')
    except:
        print('Número inválido, digite um número inteiro')
        return mostrarNumero()



mostrarNumero()