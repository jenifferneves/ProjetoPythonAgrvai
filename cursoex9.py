sal=float(input('Digite o salário do funcionário: R$'))
n= sal + (sal * 15/100)
print('O salário do funcionário que era R${:.2f}, com 15% de aumento passará a ser R${:.2f}'.format(sal, n))