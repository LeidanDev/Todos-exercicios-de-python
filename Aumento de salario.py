sal = float(input('Digite o salario: '))
porc1 = (10/100)*sal
total1 = porc1 + sal
porc2= (15/100)*sal
total2= porc2 + sal
if sal > 1250.00:
    print(f'Seu salário era {sal:.2f} \nSeu novo salario será R${total1:.2f}')
if sal <= 1250.00:
   print(f'Seu salário era {sal:.2f} \nSeu novo salario será R${total2:.2f}')
