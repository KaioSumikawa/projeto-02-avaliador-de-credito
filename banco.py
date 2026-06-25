print('bem-vindo ao banco python.')
salario_mensal = float(input('qual seu salario mensal?: '))
idade = int(input('sua idade?: '))

if idade < 18:
    print('empréstimo negado por idade')
else:
    print('idade aprovada, prosseguindo...')

valor_emprestimo = float(input('digite valor do empréstimo'))
meses = int(input('quantos meses pagar?'))

parcela = valor_emprestimo / meses

print(f'parcela mensal: R${parcela:.2f}')

if 