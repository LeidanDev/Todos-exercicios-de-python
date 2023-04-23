from datetime import date
from calendar import isleap
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if isleap(ano):
    print (f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
