from datetime import date

def leiaIdade ():
        try:
            anoAtual = date.today().year
            print('Insira seu nome completo.')
            nome = str(input())
            print('Insira seu ano de nascimento.')
            ano = int(input())
            if (ano <= 1922) or (ano > 2021):
                print('Insira uma data entre 1922 e 2021.')
                return leiaIdade()
            else:
                idade = anoAtual - ano
                print((f'Seu nome é: {nome}, sua idade é {idade}'))

        except (ValueError,TypeError):
            print('Valor inválido. Informe o ano de nascimento entre 1922 e 2021.')
            return leiaIdade()
leiaIdade()












