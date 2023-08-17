p=float(input('Preço do produto? R$'))
d= p - (p * 5/100)
print('O produto que custava R${:.2f} com a promoção de 5% vai sair por R${:.2f}'.format(p, d))