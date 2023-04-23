val = float(input('Digite o valor da casa: '))
sal = float(input('Salário do comprador: '))
pres = int(input('Quantos anos de financiamento? '))
m = 12 * pres
p = val / m
if p > 0.3 * sal:
    print ('O empréstimo foi negado!')
    print(f'Para pagar uma casa de R${val:.2f} em {pres} anos a prestação será de R${p:.2f} mensais')
elif p < 0.3 * sal:
    print('Empréstimo concedido!')
    print(f'Para pagar uma casa de R${val:.2f} em {pres} anos a prestação será de R${p:.2f} mensais')