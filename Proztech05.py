n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

print('Operações \n 1 - soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - sair')

escolha = 0
while escolha != 5:

    escolha = int(input('Escolha uma operação:'))
    print(f'Você escolheu a operação {escolha}')

    if escolha == 1:
        soma = n1 + n2
        print(f'A soma de {n1} com {n2} é igual a {soma}')

    elif escolha == 2:
        subtrai = n1 - n2
        print(f'A subtração de {n1} com {n2} é igual a {subtrai}')

    elif escolha == 3:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {multi}')


    elif escolha == 4:
        div = n1 / n2
        print(f'A divisão de {n1} e {n2} é igual a {div:.1f}')

    elif escolha == 0:
        print('Saindo...')
        break

    else:
        print('Operação invalida! Tente novamente!')








