c=int(input('Quantos dias foi alugado?'))
km=float(input('Quantos km rodados?'))
p= (c*60) + (km*0.15)
print('O total a ser pago é R${}'.format(p))